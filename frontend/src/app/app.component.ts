import { Component } from '@angular/core';
import { ApiServiceService } from './services/api-service.service';

interface Product {
  id:number,
  title:string,
  category:string,
  description:string,
  price:number,
  image:string,
  rating:{
    rate:number,
    count:number
  }
}


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'frontend';
  Products:Array<Product>=[]

  constructor (private apiServices:ApiServiceService){

  }

  buyProduct(product:Product){
    this.apiServices.getStripeUrl(product).subscribe((response)=>{
      console.log(response)
      window.location.href=response.url
    })
  }
  
  ngOnInit(){
    this.apiServices.getProducts().subscribe((respose)=>{
      console.log(respose)
      this.Products=respose
    })
  }
}
