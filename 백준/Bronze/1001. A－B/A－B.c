#include <stdio.h>

int main() {
    // 두 정수 A와 B를 입력받음
    int A, B;
    scanf("%d %d", &A, &B);

    // 입력된 두 정수의 차를 계산하고 출력
    int result = A - B;
    printf("%d\n", result);

    return 0;
}
