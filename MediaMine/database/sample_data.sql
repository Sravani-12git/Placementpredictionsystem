-- MediaMine Sample Data Insertion Script

-- Insert Categories
INSERT INTO category (id, name, description, media_category) VALUES
(1, 'Technology', 'Artificial Intelligence, software engineering, cloud computing, and hardware innovations.', 'TECH'),
(2, 'Sports', 'Global sporting events, athletics, football, basketball, and tournament analytics.', 'SPORTS'),
(3, 'Politics', 'Geopolitics, governance, international relations, policy updates, and elections.', 'POLITICS'),
(4, 'Entertainment', 'Movies, music, streaming series, digital art, and celebrity media.', 'ENTERTAINMENT'),
(5, 'Business', 'Global economy, financial markets, startup ecosystem, venture capital, and trade.', 'BUSINESS'),
(6, 'Science', 'Space exploration, quantum physics, climate science, biotechnology, and medical research.', 'SCIENCE');

-- Insert 15 Realistic Media Records
INSERT INTO media (id, title, media_type, content, transcript, caption, source, published_date, created_at) VALUES
(1, 'Breakthrough in Artificial Intelligence and Neural Networks', 'NEWS', 
 'Scientists have announced a major breakthrough in artificial intelligence models, achieving unprecedented performance in pattern matching and natural language processing tasks.', 
 'Welcome to Tech Today. Artificial intelligence models are advancing rapidly. Neural networks can now process complex string algorithms in real time.', 
 'AI models achieve record efficiency in pattern matching.', 'TechCrunch', '2026-08-15 10:00:00', '2026-08-15 10:00:00'),

(2, 'Championship Final: Epic Showdown in World Football', 'VIDEO', 
 'An thrilling final match ended with a dramatic penalty shootout as the underdogs secured their first-ever international championship trophy.', 
 'The referee blows the final whistle! What an unbelievable sports event. The crowd is roaring in the stadium as the players celebrate their historic victory.', 
 'Unbelievable football championship final highlights.', 'ESPN', '2026-08-16 18:30:00', '2026-08-16 18:30:00'),

(3, 'Global Economy Update: Inflation Dynamics and Trade Markets', 'TRANSCRIPT', 
 'Central banks around the world adjust interest rates in response to shifting global supply chains, market liquidity, and trade agreements.', 
 'This is Global Economy Insights. Today we discuss inflation dynamics, interest rate policies, and how international trade markets are reacting to fiscal changes.', 
 'Global trade markets adjust to central bank interest rate decisions.', 'Bloomberg', '2026-08-17 09:15:00', '2026-08-17 09:15:00'),

(4, 'Quantum Computing Breakthrough: Scaling Qubits', 'NEWS', 
 'Researchers demonstrate a fault-tolerant quantum computer capable of solving matrix chain multiplication and complex optimization problems in seconds.', 
 'Quantum computing technology is reaching a critical milestone. Researchers have successfully scaled qubits while maintaining coherence times.', 
 'Quantum hardware achieves new quantum supremacy benchmark.', 'MIT Technology Review', '2026-08-18 14:20:00', '2026-08-18 14:20:00'),

(5, 'Summer Blockbuster Movie Sets New Box Office Record', 'ENTERTAINMENT', 
 'The latest sci-fi movie release smashed international box office records, drawing millions of viewers over its premiere weekend.', 
 'Film critics are raving about the stunning visual effects and compelling storytelling in this summer cinematic masterpiece.', 
 'Sci-fi epic breaks opening weekend box office records.', 'Hollywood Reporter', '2026-08-19 21:00:00', '2026-08-19 21:00:00'),

(6, 'International Space Station Discovers New Exoplanet', 'NEWS', 
 'Astronomers utilizing space telescope imagery have detected an Earth-sized exoplanet located in the habitable zone of a nearby star system.', 
 'Breaking space news: deep space sensors have discovered a candidate exoplanet with atmospheric signatures indicating potential liquid water.', 
 'Astronomers detect Earth-like exoplanet in habitable zone.', 'NASA News', '2026-08-20 11:45:00', '2026-08-20 11:45:00'),

(7, 'Cybersecurity Summit: Protecting Critical Infrastructure', 'AUDIO', 
 'Global security experts gather to discuss mitigation techniques against zero-day exploits, ransom attacks, and distributed denial of service threats.', 
 'Welcome to the Security Podcast. Cybersecurity engineers are implementing advanced pattern recognition and anomaly detection algorithms across server clusters.', 
 'Experts discuss next-gen cybersecurity defense strategies.', 'Wired', '2026-08-21 16:10:00', '2026-08-21 16:10:00'),

(8, 'Global Climate Accord Signed by 150 World Leaders', 'TRANSCRIPT', 
 'World leaders have ratified a comprehensive climate agreement aiming to reduce carbon emissions and invest in renewable energy technology.', 
 'In international politics today, delegates voted overwhelmingly to adopt the landmark global sustainability framework.', 
 'Historic climate agreement signed at international summit.', 'Reuters', '2026-08-22 08:30:00', '2026-08-22 08:30:00'),

(9, 'Venture Capital Surge in Generative AI Startups', 'NEWS', 
 'Venture capital firms poured record funding into early-stage generative AI startups, driving valuation surges across the technology ecosystem.', 
 'Investors are flocking to artificial intelligence ventures building intelligent search engines, document similarity tools, and automation agents.', 
 'Venture funding reaches record high for AI startups.', 'Forbes', '2026-08-23 13:00:00', '2026-08-23 13:00:00'),

(10, 'Basketball Legend Retires After 20 Iconic Seasons', 'VIDEO', 
 'A legendary basketball career comes to an emotional end as the star athlete announces retirement in front of thousands of cheering fans.', 
 'Thank you fans for two decades of unbelievable support. It has been an honor playing this game at the highest professional level.', 
 'Iconic sports star announces retirement from basketball.', 'Sports Illustrated', '2026-08-24 20:15:00', '2026-08-24 20:15:00'),

(11, 'Advances in Gene Editing and Biotechnology', 'NEWS', 
 'Biotech researchers successfully utilize CRISPR technology to target and edit genetic sequences responsible for hereditary metabolic disorders.', 
 'Biotechnology is revolutionizing modern medicine. Precision gene editing allows scientists to repair defective DNA strands with minimal off-target effects.', 
 'Gene editing trial shows promising therapeutic results.', 'Nature Biotech', '2026-08-25 15:40:00', '2026-08-25 15:40:00'),

(12, 'Music Streaming Trends: The Rise of Independent Artists', 'AUDIO', 
 'Direct-to-fan streaming platforms empower independent musicians to reach global audiences without traditional record label contracts.', 
 'In this episode of Music Tech Weekly, we examine how recommendation algorithms and streaming analytics help indie artists monetize their work.', 
 'Independent artists leverage digital streaming analytics.', 'Billboard', '2026-08-26 12:00:00', '2026-08-26 12:00:00'),

(13, 'Electric Vehicle Battery Breakthrough Promises 600-Mile Range', 'NEWS', 
 'Solid-state battery research achieves a massive density increase, promising electric vehicles capable of traveling over 600 miles per single charge.', 
 'Clean energy technology moves forward as battery engineers solve heat dissipation and charge-cycle degradation challenges.', 
 'Solid-state EV battery achieves major energy density breakthrough.', 'Automotive News', '2026-08-27 10:30:00', '2026-08-27 10:30:00'),

(14, 'Elections Analysis: Voter Sentiment and Economic Policy', 'TRANSCRIPT', 
 'Political analysts evaluate voting patterns, polling data, and key policy debates driving voter engagement ahead of upcoming national elections.', 
 'Welcome to Politics Live. Our panel analyzes how economic policies, job growth, and public sentiment influence electoral results.', 
 'Analysts break down key policy debates ahead of national elections.', 'BBC News', '2026-08-28 17:50:00', '2026-08-28 17:50:00'),

(15, 'Next-Generation Autonomous Robotics in Logistics', 'VIDEO', 
 'Robotics engineers demonstrate autonomous warehouse units using real-time spatial path planning, string search sensor alignment, and dynamic decision trees.', 
 'Robotics technology is transforming logistics. Autonomous vehicles navigate busy distribution centers safely using onboard sensors and algorithms.', 
 'Autonomous warehouse robots streamline supply chain operations.', 'Robotics Today', '2026-08-29 14:00:00', '2026-08-29 14:00:00');

-- Map Media to Categories
INSERT INTO media_categories (media_id, category_id) VALUES
(1, 1), (1, 6),
(2, 2), (2, 4),
(3, 5), (3, 3),
(4, 1), (4, 6),
(5, 4),
(6, 6), (6, 1),
(7, 1), (7, 5),
(8, 3), (8, 6),
(9, 1), (9, 5),
(10, 2), (10, 4),
(11, 6), (11, 1),
(12, 4), (12, 1),
(13, 1), (13, 6),
(14, 3), (14, 5),
(15, 1), (15, 5);

-- Insert Sample Search Queries
INSERT INTO search_query (id, query_text, algorithm, result_count, searched_at) VALUES
(1, 'artificial intelligence', 'KMP', 3, '2026-08-30 10:00:00'),
(2, 'championship', 'Z-FUNCTION', 1, '2026-08-30 11:30:00'),
(3, 'quantum computing', 'RABIN-KARP', 1, '2026-08-30 14:15:00'),
(4, 'technology', 'AHO-CORASICK', 8, '2026-08-30 16:45:00'),
(5, 'artifical inteligence', 'QUERY-CORRECTION', 5, '2026-08-30 18:20:00');

-- Insert Sample Media Events
INSERT INTO media_event (id, media_id, event_type, event_time) VALUES
(1, 1, 'VIEW', '2026-08-30 10:01:00'),
(2, 1, 'LIKE', '2026-08-30 10:05:00'),
(3, 2, 'PLAY', '2026-08-30 11:35:00'),
(4, 2, 'SHARE', '2026-08-30 11:40:00'),
(5, 3, 'VIEW', '2026-08-30 12:00:00'),
(6, 4, 'PLAY', '2026-08-30 14:20:00'),
(7, 5, 'VIEW', '2026-08-30 15:10:00'),
(8, 9, 'LIKE', '2026-08-30 17:00:00');
