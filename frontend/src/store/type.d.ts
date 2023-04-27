// Trip interface and types
interface ITrip {
    id: number
    user: number
    startLocation: string
    endLocation: string
    startDate: Date
    endDate: Date
    flightNumber?: string
    distance: number
    lat: number
    long: number
    type: string
    notes?: string
}

type TripState = {
    trips?: ITrip[]
    [index: number]: ITrip
}

type TripAction = {
    type: string
    trip: ITrip
    trips: ITrip[]
    tripId: number
}

//General App State
interface AppState {
    trips: TripState;
}

type DispatchType = (args: TripAction) => TripAction