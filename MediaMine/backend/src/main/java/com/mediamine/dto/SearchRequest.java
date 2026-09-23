package com.mediamine.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SearchRequest {
    private String text;
    private String pattern;
    private List<String> keywords;
    private String algorithm;
    private String text1;
    private String text2;
    private String a;
    private String b;
    private Integer insertCost;
    private Integer deleteCost;
    private Integer substituteCost;
    private List<String> categories;
    private List<Integer> categoryScores;
    private Integer maxCategories;
    private List<Integer> matrixDimensions;
}
