import pdb

def bubble_sort(array):
   sorted = True
   while sorted:
      sorted = False
      for i in range(len(array)-1):
         if (array[i] > array[i+1]):
            sorted = True
            array[i], array[i+1] = array[i+1], array[i]
            pdb.set_trace()
   return array

result = bubble_sort([3, 2, 0, 1, 4, 10])
print(result)
