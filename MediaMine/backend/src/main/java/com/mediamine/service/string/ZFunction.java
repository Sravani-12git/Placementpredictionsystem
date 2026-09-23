package com.mediamine.service.string;

import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;

/**
 * Z-Function String Matching Algorithm
 * 
 * Problem: For a string S of length n, compute array Z where Z[i] is the length 
 *          of the longest common prefix between S and the suffix of S starting at i.
 * Idea: Maintain an explicit segment [L, R] representing the rightmost substring 
 *       that is also a prefix of S. Use precomputed Z values inside [L, R] to skip comparisons.
 * 
 * Algorithm Steps:
 * 1. Form concatenated string S = pattern + "$" + text.
 * 2. Compute Z-array for string S.
 * 3. Any index i >= pattern.length() + 1 where Z[i] == pattern.length() is a match position 
 *    in text at index (i - pattern.length() - 1).
 * 
 * Time Complexity: O(n) where n = |text| + |pattern|
 * Space Complexity: O(n) for Z-array.
 */
@Service
public class ZFunction {

    public int[] computeZArray(String s) {
        if (s == null || s.isEmpty()) {
            return new int[0];
        }
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;

        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }

    public List<Integer> search(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        if (text == null || pattern == null || pattern.isEmpty() || text.length() < pattern.length()) {
            return matches;
        }

        String concat = pattern + "$" + text;
        int[] z = computeZArray(concat);
        int m = pattern.length();

        for (int i = m + 1; i < concat.length(); i++) {
            if (z[i] == m) {
                matches.add(i - m - 1);
            }
        }
        return matches;
    }
}
