var reduce = function(nums, fn, init) {
    let val = 0;
    if(nums.length == 0){
        return init;
    }

    val = fn(init, nums[0]);

    for(let i = 1; i< nums.length; i++){
        val = fn(val, nums[i]);
    }
    return val;
};

// for each testcase we have different functionality for fn so here the above body is for single testcase
function fn(val, nums) {
    return val+nums;
}

reduce([1,2,3,4], fn, 0)