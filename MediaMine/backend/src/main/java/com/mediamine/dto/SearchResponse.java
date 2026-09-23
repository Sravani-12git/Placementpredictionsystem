package com.mediamine.dto;

import com.mediamine.entity.Media;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SearchResponse {
    private String query;
    private String algorithm;
    private int totalMatches;
    private long executionTimeMs;
    private List<Media> results;
    private List<Integer> matchedPositions;
    private Object metadata;
}
