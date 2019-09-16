def longestPalindrome(s):
        n = len(s)
        A = [[0 for i in range(n)] for j in range(n)] 
        for i in range (n):     
            A[i][i]=1
        for x in range (2,n+1):
            for i in range (n-x+1):
                j = i+x-1
                if (s[i]==s[j]):
                    A[i][j]=A[i+1][j-1]+2
                else:
                    A[i][j]=max(A[i][j-1], A[i+1][j])
        print (A)
        return A[0][n-1]

print ("Length of the longest palindromic subsequence is", longestPalindrome('babcbab'))

