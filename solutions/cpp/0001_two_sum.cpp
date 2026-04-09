/*
LeetCode 1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Topic: array/hash-table

Idea:
- 

Time Complexity: O(n)
Space Complexity: O(n)
*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> heap;
        int n = nums.size();
        for(int i = 0; i < n; i ++){
            int r = target - nums[i];
            if(heap.count(r))  return{heap[r], i};
            heap[nums[i]] = i;
            //给出的数字作为key,下标是value。heap[key]=value。
        }
        return {};
    }
};

