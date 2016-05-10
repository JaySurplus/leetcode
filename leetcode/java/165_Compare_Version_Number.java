class Solution {
    public int compareVersion(String version1, String version2) {
        int i = 0;
        int j = 0;

        while ( i < version1.length()|| j < version2.length()) {
            int v1 = 0;
            int v2 = 0;
            while ( i < version1.length() && version1.charAt(i) != '.') {
                v1 = v1*10 + version1.charAt(i)-'0';
                i ++ ;
            }
            while ( j < version2.length() && version2.charAt(j) != '.') {
                v2 = v2*10 + version2.charAt(j)-'0';
                j ++ ;
            }

            if (v1 > v2) return 1;
            else if (v1 < v2) return -1;

            i++;
            j++;

        }
        return 0;
    }
}


class Untitled {
    public static void main(String[] args) {
        //System.out.println(args.length);
        String v1;
        String v2;
        if (args.length == 2) {
            v1 = args[0];
            v2 = args[1];
        } else {
            v1 = "1.0";
            v2 = "2.9";
        }


        Solution sol = new Solution();
        System.out.println(sol.compareVersion(v1,v2));
    }
}
