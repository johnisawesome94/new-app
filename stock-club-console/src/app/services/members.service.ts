import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Member } from '../common/types';
import { RestConstants } from '../common/constants/rest';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MembersService {

  constructor(private httpClient: HttpClient) { }

  public getMembers(): Observable<Member[]> {
    return this.httpClient.get<Member[]>(RestConstants.MEMBERS_URL);
  }
}
