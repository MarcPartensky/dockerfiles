#include "pqcrypto_keyexchange.h"
#include "newhope.h"

int pqcrypto_keyexchange_newhope()
{
    // Initialize NewHope parameters
    PARAM_SET param_set = PARAMS_1024_60;

    // Generate Alice's key pair
    polyvec a;
    polyvec ahat;
    uint8_t senda[NEWHOPE_SENDABYTES];
    uint8_t key[NEWHOPE_KEYBYTES];

    newhope_keygen(&a, &ahat, senda, param_set);

    // Receive Bob's public key and generate shared key
    uint8_t receivedb[NEWHOPE_SENDBBYTES];
    randombytes(receivedb, NEWHOPE_SENDBBYTES);

    newhope_sharedb(key, &a, receivedb, param_set);

    // Send Alice's public key and generate shared key
    uint8_t receiveda[NEWHOPE_SENDABYTES];
    randombytes(receiveda, NEWHOPE_SENDABYTES);

    newhope_shareda(key, &ahat, receiveda, param_set);

    // Check if key exchange was successful
    if (memcmp(key, newhope_testvector_sharedkey, NEWHOPE_KEYBYTES) == 0) {
        return 0; // success
    } else {
        return -1; // failure
    }
}

