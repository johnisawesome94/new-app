import { Injectable } from '@angular/core';
import { Funds } from '../common/types';
import { RestConstants } from '../common/constants/rest';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FundsService {

  constructor(private httpClient: HttpClient) { }

  public getFunds(): Observable<any> {
    return this.httpClient.get<any>(RestConstants.FUNDS_URL);
  }

  public postFunds(contribution: string): Observable<any> {
    return this.httpClient.post<string>(RestConstants.FUNDS_URL, {userId: '6536a1b6-ee12-47c0-8a7d-42df44775e6b', amount: contribution });
  }

}
