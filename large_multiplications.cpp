#include <bits/stdc++.h>
using namespace std;

/*
    This program is used to multiply insanely large integral numbers accurately
    Eg (10^51+5)*(10^33+9)

    to multiply, we reverse the strings, then we multiply from left to right digit wise
    then we reverse the product to get final answer.

    its just like school multiplications

     12
    x12
    ----
     12
    12
    ---
    132
*/

string add(string x,string y)
{
    string a,b,c="";
    int i,k,digit,carry = 0;
    char ch;
    if(x.length() >= y.length())
    {
        a = x;
        b = y;
    }
    else
    {
        a = y;
        b = x;
    }
    reverse(a.begin(),a.end());
    reverse(b.begin(),b.end());
    for(i = b.length(); i < a.length(); i++)
    {
        b.push_back('0');
    }
    k = 0;
    for(i = 0; i < a.length()-1; i++)
    {
        digit = carry + int(a[i])+int(b[i])-96;
        ch = digit%10+48;
        carry = digit/10;
        c.push_back(ch);
        k++;
    }
    digit = carry + int(a[k])+int(b[k])-96;
    while(digit)
    {
        ch = digit%10+48;
        digit = digit/10;
        c.push_back(ch);
    }
    reverse(c.begin(),c.end());
    return c;
}

string multiply(int a,string b)
{
    int i,k=0,digit,carry = 0;
    string c = "";
    char ch;
    reverse(b.begin(),b.end());
    for(i = 0; i < b.length()-1; i++)
    {
        digit = carry + (int(b[i])-48)*a;
        ch = digit%10+48;
        c.push_back(ch);
        carry = digit/10;
        k++;
    }
    digit = carry + (int(b[k])-48)*a;
    while(digit)
    {
        ch = digit%10+48;
        c.push_back(ch);
        digit = digit/10;
    }
    reverse(c.begin(),c.end());
    return c;
}

int main(void)
{
    string a,b,res,ans="";
    int i,j,digit;
    cin >> a >> b;
    reverse(b.begin(),b.end());
    for(i = 0; i < b.length(); i++)
    {
        digit = b[i]-48;
        res = multiply(digit,a);
        for(j = 0; j < i; j++)
        {
            res.push_back('0');
        }
        ans = add(ans,res);
    }
    cout << ans << endl;
}
