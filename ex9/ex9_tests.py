import unittest
import ex9_code as main


class TestInit(unittest.TestCase):
    # test whether the init sets up the value as we need them to be.
    def test_set_init_values(self):
        input_list = [4,2,3,5]
        heap = main.Heap(input_list)
        self.assertEqual(
                heap._heap,
                [5,4,3,2])

class TestEmpty(unittest.TestCase):

    def test_if_empty(self):
        # creates an empty heap
        heap = main.Heap()
        self.assertTrue(heap.is_empty())

class TestRemoveTop(unittest.TestCase):

    def test_removal_from_empty_heap(self):
        heap = main.Heap()
        with self.assertRaises(main.HeapEmptyException,
            msg="Attempt to Remove top of empty heap"):
                heap.remove_top()

    def test_result(self):
        input_list = [5,4,3,2]
        heap = main.Heap(input_list)
        self.assertEqual(
                heap.remove_top(),
                input_list[0])

    def test_resultant_list(self):
        input_list = [2,3,1,4]
        heap = main.Heap(input_list)
        heap.remove_top()
        self.assertEqual(
                heap._heap,
                [3,2,1])





if __name__ ==  '__main__':
    unittest.main(exit = False)

