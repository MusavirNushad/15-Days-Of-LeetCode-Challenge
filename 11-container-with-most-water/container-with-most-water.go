func maxArea(height []int) int {
    left, right := 0, len(height)-1
    maxWater := 0

    for left < right {
        // width between lines
        width := right - left

        // height is limited by the shorter line
        h := height[left]
        if height[right] < h {
            h = height[right]
        }

        // calculate area
        area := width * h
        if area > maxWater {
            maxWater = area
        }

        // move the pointer with smaller height
        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }

    return maxWater
}
