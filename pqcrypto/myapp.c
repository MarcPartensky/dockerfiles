#include <stdio.h>
#include "pqcrypto_keyexchange.h"

int main()
{
    // Perform key exchange using NewHope
    int status = pqcrypto_keyexchange_newhope();

    if (status == 0) {
        printf("Key exchange successful!\n");
    } else {
        printf("Key exchange failed.\n");
    }

    return 0;
}

