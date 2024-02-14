func search(nums []int, target int) int {
  // left and right pointers
  l, r := 0, len(nums)-1
  // while loop
  for l <= r {
    mid := (l + r)/2
    // fmt.Println(mid, "mid")
    if nums[mid] < target {
      l = mid + 1
    } else if nums[mid] > target {
      r = mid - 1 
    } else {
      return mid
    }
  }

  return -1
}