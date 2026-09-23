package com.mediamine.service.string;

import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;

/**
 * Rabin-Karp Rolling Hash String Search Algorithm
 * 
 * Problem: Find all starting indices of pattern P of length m in text T of length n using hashing.
 * Idea: Treat strings as numerical values using polynomial rolling hash functions. 
 *       When window hash matches pattern hash, verify character-by-character to eliminate hash collisions.
 * 
 * Algorithm Steps:
 * 1. Compute hash value of pattern and first window of text of length m.
 * 2. Slide window across text one position at a time.
 * 3. Update rolling hash in O(1) time: hash_new = (d * (hash_old - T[i]*h) + T[i+m]) mod q.
 * 4. On hash match, perform character comparison verification.
 * 
 * Time Complexity: Average O(n + m), Worst O(n * m) on heavy hash collisions.
 * Space Complexity: O(1) auxiliary space.
 */
@Service
public class RabinKarp {

    private static final int PRIME_BASE = 256;
    private static final long MODULUS = 1000000007L;

    public List<Integer> search(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        if (text == null || pattern == null || pattern.isEmpty() || text.length() < pattern.length()) {
            return matches;
        }

        int n = text.length();
        int m = pattern.length();
        long pHash = 0; // hash value for pattern
        long tHash = 0; // hash value for text window
        long h = 1;     // d^(m-1) % MODULUS

        for (int i = 0; i < m - 1; i++) {
            h = (h * PRIME_BASE) % MODULUS;
        }

        for (int i = 0; i < m; i++) {
            pHash = (PRIME_BASE * pHash + pattern.charAt(i)) % MODULUS;
            tHash = (PRIME_BASE * tHash + text.charAt(i)) % MODULUS;
        }

        for (int i = 0; i <= n - m; i++) {
            if (pHash == tHash) {
                // Character by character verification on hash match
                boolean collisionVerify = true;
                for (int j = 0; j < m; j++) {
                    if (text.charAt(i + j) != pattern.charAt(j)) {
                        collisionVerify = false;
                        break;
                    }
                }
                if (collisionVerify) {
                    matches.add(i);
                }
            }

            if (i < n - m) {
                tHash = (PRIME_BASE * (tHash - text.charAt(i) * h) + text.charAt(i + m)) % MODULUS;
                if (tHash < 0) {
                    tHash = (tHash + MODULUS);
                }
            }
        }
        return matches;
    }
}
