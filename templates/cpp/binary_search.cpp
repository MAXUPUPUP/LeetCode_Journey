#include <vector>
using namespace std;

int lower_bound_index(const vector<int>& nums, int target) {
    int left = 0, right = (int)nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}

int upper_bound_index(const vector<int>& nums, int target) {
    int left = 0, right = (int)nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
