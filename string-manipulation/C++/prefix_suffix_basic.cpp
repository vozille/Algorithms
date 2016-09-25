a[n];
pre[n+2];
suf[n+2];
for(int i = 0; i < (n+1); i++)
{
  pre[i] = function(pre[i-1],a[i-1]);
}
for(int i = n; i > 0; i--)
{
  suf[i] = function(suf[i+1],a[i-1]);
}
for(int i = 1; i <= n; i++)
{
  something(pre[i-1],a[i-1],suf[i+1]);
}
