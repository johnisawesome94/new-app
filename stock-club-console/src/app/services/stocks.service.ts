import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RestConstants } from '../common/constants/rest';
import { Observable } from 'rxjs';
import { Stock } from '../common/types';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class StocksService {

  constructor(private httpClient: HttpClient) { }

  public getStocks(): Observable<Stock[]> {
    return this.httpClient.get<Stock[]>(RestConstants.STOCKS_URL);
  }

  public searchStocks(search: string): Observable<any> {
    return this.httpClient.get<any>(`${RestConstants.STOCKS_URL}/${search}`).pipe(
      map(results => results[0])
    );
  }

  public postMember(newStock: Stock): Observable<Stock> {
    return this.httpClient.post<Stock>(RestConstants.STOCKS_URL, newStock);
  }

  public deleteMember(stockId: string): Observable<any> {
    return this.httpClient.delete(`${RestConstants.STOCKS_URL}/${stockId}`, { responseType: 'text' });
  }
}
