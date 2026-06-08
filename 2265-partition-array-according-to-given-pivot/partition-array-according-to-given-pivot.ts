function pivotArray(nums: number[], pivot: number): number[] {
    const smaller: number[] = [];
    const equal: number[] = [];
    const greater:number[]=[];

    for (let i=0; i<nums.length; i++){
        if (nums[i]<pivot){
            smaller.push(nums[i]);
        }
        else if (nums[i]==pivot){
            equal.push(nums[i]);
        }
        else{
            greater.push(nums[i]);
        }
    }

    return [...smaller, ...equal, ...greater];
};