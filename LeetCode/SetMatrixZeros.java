import java.util.ArrayList;

public class SetMatrixZeros {

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 1, 1},
            {1, 0, 1},
            {1, 1, 0}
        };
        ArrayList<ArrayList<Integer>> indexValues = new ArrayList<>();

        for (int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    ArrayList<Integer> indexValue = new ArrayList<>();
                    indexValue.add(i);
                    indexValue.add(j);
                    indexValues.add(indexValue);
                }
            }
        }
        System.out.println(indexValues);

        for (ArrayList<Integer> indexValue : indexValues) {
            int row = indexValue.get(0);
            int col = indexValue.get(1);
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][col] = 0;
            }
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[row][j] = 0;
            }
        }   


    }
}