//Trips action types
const ADD_TRIPS = 'ADD_TRIPS'
const ADD_TRIP = 'ADD_TRIP'
const REMOVE_TRIP = 'REMOVE_TRIP' 

//Trips actions
const addTrips = (trips: ITrip[]) => ({
    type: ADD_TRIPS,
    trips
})

const addTrip = (trip: ITrip) => ({
    type: ADD_TRIP,
    trip
})

const removeTrip = (tripId: number) => ({
    type: REMOVE_TRIP,
    tripId
})

//Trips fetch requests
const initialState = {}
//Trips reducer
export const tripsReducer = (
    state: TripState = initialState,
    action: TripAction
): TripState => {
    switch (action.type) {
        case ADD_TRIPS:
            return { ...action.trips };
        case ADD_TRIP:
            return {
                ...state,
                [action.trip.id]: action.trip
            }
        case REMOVE_TRIP:
            let newState = { ...state };
            delete newState[action.tripId];
            return newState;
    }
    return state
}