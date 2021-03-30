import random


class MatrixMultiplication(object):

    def recursive_matrix_multiply(self, n, first, second):
        if n <= 16:
            return self.naive_matrix_multiply(n, first, second)

        [a, b, c, d] = self.split_matrix_in_quads(first)
        [e, f, g, h] = self.split_matrix_in_quads(second)

        half = int(n / 2)
        q1 = self.add_matrices(self.recursive_matrix_multiply(half, a, e), self.recursive_matrix_multiply(half, b, g))
        q2 = self.add_matrices(self.recursive_matrix_multiply(half, a, f), self.recursive_matrix_multiply(half, b, h))
        q3 = self.add_matrices(self.recursive_matrix_multiply(half, c, e), self.recursive_matrix_multiply(half, d, g))
        q4 = self.add_matrices(self.recursive_matrix_multiply(half, c, f), self.recursive_matrix_multiply(half, d, h))

        return self.join_quads_into_matrix(q1, q2, q3, q4)

    def strassen_matrix_multiply(self, n, first, second):
        if n <= 16:
            return self.naive_matrix_multiply(n, first, second)

        [a, b, c, d] = self.split_matrix_in_quads(first)
        [e, f, g, h] = self.split_matrix_in_quads(second)

        half = int(n / 2)

        p1 = self.strassen_matrix_multiply(half, a, self.subtract_matrices(f, h))
        p2 = self.strassen_matrix_multiply(half, self.add_matrices(a, b), h)
        p3 = self.strassen_matrix_multiply(half, self.add_matrices(c, d), e)
        p4 = self.strassen_matrix_multiply(half, d, self.subtract_matrices(g, e))
        p5 = self.strassen_matrix_multiply(half, self.add_matrices(a, d), self.add_matrices(e, h))
        p6 = self.strassen_matrix_multiply(half, self.subtract_matrices(b, d), self.add_matrices(g, h))
        p7 = self.strassen_matrix_multiply(half, self.add_matrices(a, c), self.add_matrices(e, f))

        q1 = self.add_matrices(p5, p4)
        q1 = self.subtract_matrices(q1, p2)
        q1 = self.add_matrices(q1, p6)
        q2 = self.add_matrices(p1, p2)
        q3 = self.add_matrices(p3, p4)
        q4 = self.add_matrices(p1, p5)
        q4 = self.subtract_matrices(q4, p3)
        q4 = self.subtract_matrices(q4, p7)

        return self.join_quads_into_matrix(q1, q2, q3, q4)

    def naive_matrix_multiply(self, n, a, b):
        matrix = self.create_square_matrix(n)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    matrix[i][j] = matrix[i][j] + a[i][k] * b[k][j]

        return matrix

    @staticmethod
    def create_square_matrix(n):
        val = [0] * n
        for x in range(n):
            val[x] = [0] * n
        return val

    @staticmethod
    def create_random_square_matrix(n):
        val = [0] * n
        for x in range(n):
            val[x] = [0] * n

        for y in range(n):
            for z in range(n):
                val[y][z] = random.randint(1, 20)
        return val

    def split_matrix_in_quads(self, matrix):
        n = len(matrix)
        half = int(n / 2)
        q1 = self.create_square_matrix(half)
        q2 = self.create_square_matrix(half)
        q3 = self.create_square_matrix(half)
        q4 = self.create_square_matrix(half)

        for i in range(half):
            for j in range(half):
                q1[i][j] = matrix[i][j]
                q2[i][j] = matrix[i][j + half]
                q3[i][j] = matrix[i + half][j]
                q4[i][j] = matrix[i + half][j + half]
        return q1, q2, q3, q4

    def join_quads_into_matrix(self, q1, q2, q3, q4):
        n = len(q1)
        m = len(q1) * 2
        matrix = self.create_square_matrix(m)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = q1[i][j]
                matrix[i][j + n] = q2[i][j]
                matrix[i + n][j] = q3[i][j]
                matrix[i + n][j + n] = q4[i][j]

        return matrix

    @staticmethod
    def parse_matrix_text(path):
        array = []
        with open(path) as text:
            lines = text.readlines()
            for line in lines:
                line = line.replace('\n', '')
                new_line = line.split('\t')
                new_line.pop()
                num_line = []
                for num in new_line:
                    num_line.append(int(num))
                array.append(num_line)
        return array

    @staticmethod
    def add_matrices(a, b):
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

    @staticmethod
    def subtract_matrices(a, b):
        return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

# Profiling stuff https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/
