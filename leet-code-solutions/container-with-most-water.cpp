class Solution {
public:
    int maxArea(vector<int>& height) {
       int n=height.size();
       int water=0,i=0,j=n-1;
       while(i<j)
       {
           
           int h=min(height[i],height[j]);
           water=max(water,h*(j-i));
           if(height[i]<height[j])i++;
           else j--;
       }return water;
    }
};