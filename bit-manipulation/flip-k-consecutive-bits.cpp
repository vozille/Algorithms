#include <iostream>
#include <vector>

using namespace std;

const int INF = 1000000000;

int flips(vector<int> bit_sequence, int flipper_size, int what_bit) {
  int temp[bit_sequence.size()];
  for(int i = 0; i < bit_sequence.size(); i++){
      temp[i] = 0;
  }
  int sum=0, ans=0;
  for(int i = 0; i < bit_sequence.size(); i++) {
    temp[i] = (bit_sequence[i]+sum)%2 != what_bit;
    sum += temp[i] - (i>=flipper_size-1?temp[i-flipper_size+1]:0);
    ans += temp[i];
    if(i>bit_sequence.size()-flipper_size and temp[i]!=0) return INF;
  }
  return ans;
}

int main() {
    vector<int> bits;
    bits.push_back(1);bits.push_back(1);bits.push_back(1);
    bits.push_back(0);bits.push_back(0);bits.push_back(1);
    int flipper_size = 2;
    int ans = flips(bits, flipper_size, 1);
    cout << ans << endl;
}