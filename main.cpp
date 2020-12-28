#include <iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

void In(int num, vector<int> &a){
    for(int i=0; i<a.size(); i++){
        if(a[i] == 0){
            a[i]=num;
            break;
        }
    }
}

void Out(int num, vector<int> &a){
    for(int i=0; i<a.size(); i++){
        if(a[i] == num*(-1)){
            a[i]=0;
        }
    }
}

void OutPut(vector<int> &a){
    for(int i=0; i<a.size(); i++){
        if(a[i] !=0)
            cout<<i+1<<" "<<a[i]<<endl;
    }
}

void SizeUp(vector<int> &b){
    int a= b.size();
    vector<int>::iterator iter;
    iter=find(b.begin(),b.end(),0);
    if(iter == b.end())
       b.resize(2*a,0);
}


void SizeDown(vector<int> &b){
    int cnt=0;
    int temp=0;
    for(int i=0; i<b.size(); i++){
        if(b[i] != 0)
            cnt+=1;
    }
    vector<int>tmp(b.size(),0);
    if(cnt<=b.size()/3){
        for(int i=0; i<b.size(); i++){
           if(b[i]!=0){
              tmp[temp] = b[i];
              temp++;
            }
        }
        if(b.size()%2==1)
            tmp.resize(b.size()/2+1);
        else
            tmp.resize(b.size()/2);
    b=tmp;
    }
}

int main()
{
    int slot, N,w;
    cin>>slot;
    cin>>N;
    vector<int> k(slot,0);
    for(int i=0; i<N; i++){
        cin>>w;
        if(w>0){
            In(w,k);
            SizeUp(k);
        }
        else if(w<0){
            Out(w,k);
        }
    }
    SizeDown(k);
    OutPut(k);
    return 0;
}
