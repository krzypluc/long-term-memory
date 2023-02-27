interface SearchResponse {
    data: Array<Person>;
}

interface Person {
    firstname: string
    surname: string
    position: string
    date_of_birth: Date
    description: string
}

export type { SearchResponse, Person };