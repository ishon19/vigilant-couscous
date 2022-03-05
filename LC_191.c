// This solution beats 100% of c submissions and runs in 0 ms.

int hammingWeight(uint32_t n) {
    return n == 0? 0: (n & 1) + hammingWeight(n>>1);
}