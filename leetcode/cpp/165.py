/**
*    165. Compare Version Numbers
*/
class Solution {
public:
    int compareVersion(string version1, string version2) {

        string v1 = version1;
        string v2 = version2;

        if(v1.length() == 0 || v2.length() == 0)
            return 0;

        int i=0;
        int j=0;

        int n1;
        int n2;

        while(i<v1.length() || j<v2.length())
        {
            n1 = 0;
            n2 = 0;

            while(i<v1.length() && v1[i] != '.')
            {
                n1 = n1*10+(v1[i]-'0');
                i++;
            }

            while(j<v2.length() && v2[j] != '.')
            {
                n2 = n2*10+(v2[j]-'0');
                j++;
            }

            if(n1>n2)
                return 1;
            else if(n1<n2)
                return -1;

            if(v1[i] == '.')
                i++;
            if(v2[j] == '.')
                j++;
        }

        return 0;
    }
};
