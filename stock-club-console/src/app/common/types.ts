export class Member {
    constructor(
        public id: string,
        public firstName: string,
        public lastName: string,
        public username: string,
        public email: string) {}
}

export class NewMember {
    constructor(
        public firstName: string,
        public lastName: string,
        public email: string) {}
}

export class RegisterUser {
    constructor(
        public firstName: string,
        public lastName: string,
        public email: string,
        public password: string) {}
}

export class Funds {
    constructor(
        public total: number,
        public available: number,
        public used: number,
        public pending: number) {}
}

export class User {
    id: number;
    username: string;
    password: string;
    firstName: string;
    lastName: string;
    token: string;
    sub: string;
}
