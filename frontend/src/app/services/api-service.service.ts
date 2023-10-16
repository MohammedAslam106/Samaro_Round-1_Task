import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {

  constructor(private http:HttpClient) { }

  getProducts(){
    return this.http.get<any>('http://localhost:8000/api/products')
  }

  getStripeUrl(data:any){
    return this.http.post<any>('http://localhost:8000/payment',data)
  }
}
