#include <iostream>
#include <map>  // need c++11, c++14, or c++17
#include <string>
#include <vector>
#include <utility>

using namespace std;

typedef int Amount;
typedef int Coin;
typedef int Count;

// An empty Breakdown indicates failure.
// Otherwise, all Breakdowns contain on entry
// per Coin value.
typedef map<Coin,Count> Breakdown;

int countCoins (const Breakdown& breakdown)
{
  int result = 0;
  for (auto tuple : breakdown) {
    result += get<1>(tuple);
  }
  return result;
}

Breakdown makeChange_inner (const Amount&          amount,     // const ref: input
                            const vector<Coin>&    coins,      // const ref: input
                            map<Amount,Breakdown>& scratchpad) // non-const ref: input/output
{
  if (scratchpad.count(amount) == 0) {
    // Default to empty Breakdown (failure)
    Breakdown bestBreakdown;

    // Base Case: make change for zero
    if (amount == 0) {
      for (auto coin : coins) {
        bestBreakdown.insert({coin,0});
      }
    }
    // Recursive Case: try each Coin and save the best
    else if (amount > 0) {
      for (auto curCoin : coins) {
        if (amount >= curCoin) {
          Breakdown curBreakdown = makeChange_inner(amount-curCoin, coins, scratchpad);
          if (curBreakdown.size() == 0) {
            continue;
          }

          curBreakdown.at(curCoin) += 1;

          if ( (bestBreakdown.size() == 0 ) ||
               (countCoins(curBreakdown) < countCoins(bestBreakdown)) ) {
            bestBreakdown = curBreakdown;
          }
        }
      }
    }

    scratchpad.insert({amount,bestBreakdown});
  }

  return scratchpad.at(amount);
}

Breakdown makeChange (const Amount& amount, const vector<Coin>& coins)
{
  map<Amount,Breakdown> scratchpad;

  makeChange_inner(amount, coins, scratchpad);

  return scratchpad.at(amount);
}

void printBreakdown (const Amount& amount, const Breakdown& breakdown) {
  cout << string(40, '-') << endl;
  cout << amount << " = " << endl;
  for (auto iter = breakdown.rbegin(); iter != breakdown.rend(); ++iter) {
    cout  << "("
          << iter->first
          << ","
          << iter->second
          << ") ";
  }
  cout << endl;
  cout << string(40, '-') << endl;
}

int main ()
{
  vector<Coin> coins {1,3,10};
  vector<Amount> amounts {-3,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,56,1024};

  for (auto amount : amounts) {
    auto breakdown = makeChange(amount, coins);
    printBreakdown(amount, breakdown);
  }
}