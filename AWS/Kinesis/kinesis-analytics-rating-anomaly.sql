CREATE OR REPLACE STREAM "TEMP_STREAM" (
   "favoritecaptain" VARCHAR(16),
   "rating"        INTEGER,
   "ANOMALY_SCORE"  DOUBLE);

CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
   "favoritecaptain" VARCHAR(16),
   "rating"        INTEGER,
   "ANOMALY_SCORE"  DOUBLE);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "TEMP_STREAM"
SELECT STREAM "favoritecaptain", "rating", "ANOMALY_SCORE" FROM
  TABLE(RANDOM_CUT_FOREST(
    CURSOR(SELECT STREAM "favoritecaptain", "rating" FROM "SOURCE_SQL_STREAM_001")
  )
);
-- Sort records by descending anomaly score, insert into output stream
CREATE OR REPLACE PUMP "OUTPUT_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM * FROM "TEMP_STREAM"
ORDER BY FLOOR("TEMP_STREAM".ROWTIME TO SECOND), ANOMALY_SCORE DESC;