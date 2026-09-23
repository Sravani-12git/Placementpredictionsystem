package com.mediamine.service.suffix;

import org.springframework.stereotype.Service;
import java.util.Arrays;

/**
 * SA-IS (Suffix Array Induced Sorting) Algorithm
 * 
 * Problem: Construct Suffix Array for a string in deterministic linear time O(n).
 * Idea: Classify suffixes into S-type and L-type, identify LMS (Leftmost S) characters, 
 *       and use induced sorting bucket sorting passes.
 * 
 * Algorithm Steps:
 * 1. Classify each character i as S-type (if S[i..] < S[i+1..]) or L-type.
 * 2. Identify LMS-characters (S-type characters immediately following an L-type character).
 * 3. Perform induced sorting pass to place LMS suffixes into buckets.
 * 4. Recursively solve for LMS substrings if LMS substrings are not all unique.
 * 5. Induce complete Suffix Array from ordered LMS suffixes.
 * 
 * Time Complexity: O(n) guaranteed linear time.
 * Space Complexity: O(n) workspace arrays.
 */
@Service
public class SAIS {

    public int[] buildSuffixArray(String text) {
        if (text == null || text.isEmpty()) {
            return new int[0];
        }
        // Append sentinel character 0 to ensure uniqueness
        int n = text.length();
        int[] s = new int[n + 1];
        for (int i = 0; i < n; i++) {
            s[i] = (int) text.charAt(i) + 1;
        }
        s[n] = 0; // Sentinel

        int maxChar = 256 + 2;
        int[] saWithSentinel = sais(s, maxChar);

        // Strip the sentinel index at pos 0
        int[] sa = new int[n];
        System.arraycopy(saWithSentinel, 1, sa, 0, n);
        return sa;
    }

    private int[] sais(int[] s, int K) {
        int n = s.length;
        int[] sa = new int[n];
        if (n == 1) {
            sa[0] = 0;
            return sa;
        }

        boolean[] isS = new boolean[n];
        isS[n - 1] = true;
        for (int i = n - 2; i >= 0; i--) {
            if (s[i] < s[i + 1]) {
                isS[i] = true;
            } else if (s[i] > s[i + 1]) {
                isS[i] = false;
            } else {
                isS[i] = isS[i + 1];
            }
        }

        int[] lms = new int[n];
        int lmsCount = 0;
        for (int i = 1; i < n; i++) {
            if (isS[i] && !isS[i - 1]) {
                lms[lmsCount++] = i;
            }
        }

        int[] bucket = new int[K];
        for (int val : s) bucket[val]++;

        induce(s, sa, isS, lms, lmsCount, K, bucket);

        // Compact LMS substrings to check uniqueness
        int[] lmsMap = new int[n];
        Arrays.fill(lmsMap, -1);
        int sortedLmsCount = 0;
        for (int i = 0; i < n; i++) {
            if (sa[i] > 0 && isS[sa[i]] && !isS[sa[i] - 1]) {
                lmsMap[sortedLmsCount++] = sa[i];
            }
        }

        int currentName = 0;
        int[] names = new int[lmsCount];
        names[0] = 0;

        for (int i = 1; i < lmsCount; i++) {
            int pos1 = lmsMap[i - 1];
            int pos2 = lmsMap[i];
            boolean diff = false;
            for (int d = 0; ; d++) {
                if (s[pos1 + d] != s[pos2 + d] || isS[pos1 + d] != isS[pos2 + d]) {
                    diff = true;
                    break;
                }
                if (d > 0 && (isS[pos1 + d] && !isS[pos1 + d - 1]) && (isS[pos2 + d] && !isS[pos2 + d - 1])) {
                    break;
                }
            }
            if (diff) currentName++;
            // Map pos to index in lms array
            for (int j = 0; j < lmsCount; j++) {
                if (lms[j] == pos2) {
                    names[j] = currentName;
                    break;
                }
            }
        }

        int[] summarySa;
        if (currentName < lmsCount - 1) {
            summarySa = sais(names, currentName + 1);
        } else {
            summarySa = new int[lmsCount];
            for (int i = 0; i < lmsCount; i++) {
                summarySa[names[i]] = i;
            }
        }

        int[] orderedLms = new int[lmsCount];
        for (int i = 0; i < lmsCount; i++) {
            orderedLms[i] = lms[summarySa[i]];
        }

        induce(s, sa, isS, orderedLms, lmsCount, K, bucket);
        return sa;
    }

    private void induce(int[] s, int[] sa, boolean[] isS, int[] lms, int lmsCount, int K, int[] bucket) {
        int n = s.length;
        Arrays.fill(sa, -1);

        int[] heads = new int[K];
        int[] tails = new int[K];
        getBuckets(bucket, heads, tails);

        // Put LMS suffixes at end of buckets
        for (int i = lmsCount - 1; i >= 0; i--) {
            int pos = lms[i];
            int c = s[pos];
            sa[tails[c]--] = pos;
        }

        getBuckets(bucket, heads, tails);
        // Induce L-type
        for (int i = 0; i < n; i++) {
            if (sa[i] > 0) {
                int j = sa[i] - 1;
                if (!isS[j]) {
                    int c = s[j];
                    sa[heads[c]++] = j;
                }
            }
        }

        getBuckets(bucket, heads, tails);
        // Induce S-type
        for (int i = n - 1; i >= 0; i--) {
            if (sa[i] > 0) {
                int j = sa[i] - 1;
                if (isS[j]) {
                    int c = s[j];
                    sa[tails[c]--] = j;
                }
            }
        }
    }

    private void getBuckets(int[] bucket, int[] heads, int[] tails) {
        int sum = 0;
        for (int i = 0; i < bucket.length; i++) {
            heads[i] = sum;
            sum += bucket[i];
            tails[i] = sum - 1;
        }
    }
}
