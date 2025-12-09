public class Prefix {
    public int[] prefixSum(int[] arr) {
        int n = arr.length;
        int[] prefix = new int[n];
        
        prefix[0] = arr[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + arr[i];
        }
        
        return prefix;
    }
    
    public static void main(String[] args) {
        Prefix p = new Prefix();
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = p.prefixSum(arr);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
