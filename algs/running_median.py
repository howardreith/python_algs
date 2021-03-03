class RunningMedian(object):
    def running_median(self, min_heap, max_heap, value):
        if min_heap.peek() == None:
            min_heap.insert(value)
        elif max_heap.peek() == None and value > min_heap.peek():
            max_heap.insert(value)
        elif value <= min_heap.peek():
            min_heap.insert(value)
        else:
            max_heap.insert(value)

        self.balance_heaps(min_heap, max_heap)

        n = min_heap.get_size() + max_heap.get_size()

        if n % 2 == 0:
            first_value = min_heap.peek()
            second_value = max_heap.peek()
            return (first_value + second_value) / 2
        else:
            if min_heap.get_size() > max_heap.get_size():
                return min_heap.peek()
            else:
                return max_heap.peek()

    def balance_heaps(self, min_heap, max_heap):
        while self.is_balanced(min_heap, max_heap) is False:
            if min_heap.get_size() > max_heap.get_size():
                max_heap.insert(min_heap.extract())
            else:
                min_heap.insert(max_heap.extract())

    def is_balanced(self, min_heap, max_heap):
        min_heap_size = min_heap.get_size()
        max_heap_size = max_heap.get_size()
        n = min_heap_size + max_heap_size

        if n % 2 == 0:
            return min_heap_size == max_heap_size
        else:
            return abs(min_heap_size - max_heap_size) == 1

    def maintain_sliding_window(self, min_heap, max_heap, window, value, max_sliding_window=100):
        window.append(value)
        if len(window) <= max_sliding_window:
            return
        to_remove = window[0]
        if to_remove >= max_heap.peek():
            max_heap.delete(to_remove)
        else:
            min_heap.delete(to_remove)
        del window[0]

    def parse_text_file(self, path):
        with open(path) as text:
            lines = text.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].replace('\n', '')
                lines[i] = float(lines[i])
            return lines

    def running_median_with_sliding_window(self, min_heap, max_heap, value, window, max_sliding_window=100):
        if min_heap.peek() == None:
            min_heap.insert(value)
        elif max_heap.peek() == None and value > min_heap.peek():
            max_heap.insert(value)
        elif value <= min_heap.peek():
            min_heap.insert(value)
        else:
            max_heap.insert(value)

        self.maintain_sliding_window(min_heap, max_heap, window, value, max_sliding_window)
        self.balance_heaps(min_heap, max_heap)

        n = min_heap.get_size() + max_heap.get_size()

        if n % 2 == 0:
            first_value = min_heap.peek()
            second_value = max_heap.peek()
            return (first_value + second_value) / 2
        else:
            if min_heap.get_size() > max_heap.get_size():
                return min_heap.peek()
            else:
                return max_heap.peek()
