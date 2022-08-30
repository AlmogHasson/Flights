import axios from "axios";
const MY_URL = 'http://127.0.0.1:8000/'


export function getCountries() {
    return new Promise((resolve) =>
        axios.get(`${MY_URL}countries/`).then((res) => resolve({ data: res.data }))
    );
}
