public class Main {
    public static void main(String[] args) {
        String st, st_copy;
        for(int i=10;i<50;i++) {
            st=Integer.toString(i);
            st_copy=new StringBuffer(st).reverse().toString();
            if(!st.contains("8")) { 
                if((st.charAt(0)-48+st.charAt(1)-48)%6==0 && Integer.parseInt(st_copy)%4==0) {
                    System.out.print(i);
                    break;
                }
            }
        }
    }
}