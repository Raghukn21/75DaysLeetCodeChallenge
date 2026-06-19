#include <stdio.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int trap(int* height, int heightSize) {
    if (height == NULL || heightSize <= 2) {
        return 0;
    }

    int left = 0;
    int right = heightSize - 1;
    int leftMax = height[left];
    int rightMax = height[right];
    int water = 0;

    while (left < right) {
        // We move the pointer pointing to the smaller maximum height
        if (leftMax < rightMax) {
            left++;
            leftMax = MAX(leftMax, height[left]);
            water += (leftMax - height[left]);
        } else {
            right--;
            rightMax = MAX(rightMax, height[right]);
            water += (rightMax - height[right]);
        }
    }

    return water;
}