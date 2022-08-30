import axios from "axios";
const MY_URL = 'http://127.0.0.1:8000/'


// async(2) ----------------------------------------------------------   GET ALL FLIGHTS -------------------------------------------------
export function getFlights() {
    return new Promise((resolve) =>
        axios.get(`${MY_URL}flights/`).then((res) => resolve({ data: res.data }))
    );
}

// export function addFlight(newFlight) {
//   return new Promise((resolve) =>
//     axios.post(MY_URL, newFlight).then((res) => resolve({ data: res.data }))
//   );
// }

// export function register(newFlight) {
//     return new Promise((resolve) =>
//         axios.post(MY_URL, JSON.stringify(username,email,password)).then((res) => resolve({ data: res.data }))
//     );
// }



// export function deleteFlight(newFlight) {
//   return new Promise((resolve) =>
//     axios(MY_URL).then((res, newFlight) => resolve({ data: res.data }))
//   );
// }


// export function updateFlight(newFlight) {
//   return new Promise((resolve) =>
//     axios.put(MY_URL).then((res, newFlight) => resolve({ data: res.data }))
//   );
// }



