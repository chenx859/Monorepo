CREATE TABLE flights (
    id VARCHAR(255) PRIMARY KEY,
    flight_date DATE,
    flight_status VARCHAR(255),
    departure_airport VARCHAR(255),
    departure_timezone VARCHAR(255),
    departure_iata VARCHAR(255),
    departure_icao VARCHAR(255),
    departure_terminal VARCHAR(255),
    departure_gate VARCHAR(255),
    departure_delay INTEGER,
    departure_scheduled TIMESTAMP,
    departure_estimated TIMESTAMP,
    departure_actual TIMESTAMP,
    departure_estimated_runway TIMESTAMP,
    departure_actual_runway TIMESTAMP,
    arrival_airport VARCHAR(255),
    arrival_timezone VARCHAR(255),
    arrival_iata VARCHAR(255),
    arrival_icao VARCHAR(255),
    arrival_terminal VARCHAR(255),
    arrival_gate VARCHAR(255),
    arrival_baggage VARCHAR(255),
    arrival_delay INTEGER,
    arrival_scheduled TIMESTAMP,
    arrival_estimated TIMESTAMP,
    arrival_actual TIMESTAMP,
    arrival_estimated_runway TIMESTAMP,
    arrival_actual_runway TIMESTAMP,
    airline_id VARCHAR(255),
    flight_number VARCHAR(255),
    codeshared_flight_id VARCHAR(255)
);

CREATE TABLE airlines (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    iata VARCHAR(255),
    icao VARCHAR(255)
);

CREATE TABLE flights_codeshared (
    id VARCHAR(255) PRIMARY KEY,
    airline_id VARCHAR(255),
    flight_number VARCHAR(255),
    flight_iata VARCHAR(255),
    flight_icao VARCHAR(255)
);