CREATE TABLE PARKING_GUEST(
    ID VARCHAR2(15)    NOT NULL,
    CAR_NUMBER_VISIT    VARCHAR2(20) NOT NULL,
    PHONE_NUMBER_VISIT    NUMBER NOT NULL,
    PARKING_STATE_VISIT    VARCHAR2(20) NOT NULL,
    PARKING_ENTRANCE_TIME_VISIT    DATE NOT NULL,
    PARKING_EXIT_TIME_VISIT    DATE NOT NULL,
    ADDRESS_VISIT   	VARCHAR2(15) NOT NULL
);