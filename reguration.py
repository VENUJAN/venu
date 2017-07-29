void get2NonRepeatingNos(int arr[], int v, int *x, int *y)
{
  int xor = arr[0]; 
  int set_bit_no;  
  int i;
  *x = 0;
  *y = 0;
  for(i = 1; i < v; i++)
   xor ^= arr[i];
  set_bit_no = xor & ~(xor-1);
    
  for(i = 0; i < v; i++)
  {
    if(arr[i] & set_bit_no)
     *x = *x ^ arr[i]; /*XOR of first set */
    else
     *y = *y ^ arr[i]; /*XOR of second set*/
  }
}
 
int main()
{
  int arr[] = {2, 3, 7, 9, 11, 2, 3, 11};
  int *x = (int *)malloc(sizeof(int));
  int *y = (int *)malloc(sizeof(int));
  get2NonRepeatingNos(arr, 8, x, y);
  printf("The non-repeating elements are %d and %d", *x, *y);
  getchar();
}
