package com.mediamine.entity;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "media_event")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class MediaEvent {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "media_id")
    private Long mediaId;

    @Column(name = "event_type", nullable = false)
    private String eventType; // VIEW, PLAY, PAUSE, LIKE, SHARE, SEARCH

    @Column(name = "event_time")
    private LocalDateTime eventTime;

    @PrePersist
    protected void onCreate() {
        if (eventTime == null) {
            eventTime = LocalDateTime.now();
        }
    }
}
