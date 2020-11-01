#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

typedef pair<double,double> pdd;

int N;



double norm(pdd x, pdd y){
    return sqrt((x.first-y.first)*(x.first-y.first) + (x.second-y.second)*(x.second-y.second));
}
bool compare_x(pdd lft, pdd rht){
    return lft.first < rht.first;
}
bool compare_y(pdd lft, pdd rht){
    return lft.second < rht.second;
}

pair<pdd, pdd>rcp(vector<pdd>px, vector<pdd>py){
    if(px.size() <= 3){
        pdd b1, b2;
        double best = 1000000.0;
        for(int i = 0;i < px.size();i++){
            for(int j = i+1;j < px.size();j++){
                if(best > norm(px[i], px[j])){
                    best = norm(px[i], px[j]);
                    b1 = px[i];
                    b2 = px[j];
                }
            }
        }
    } else {

    }
}

pair< pdd, pdd >closest_pair(vector< pdd >pts){
    vector< pdd >px(pts.begin(), pts.end());
    vector< pdd >py(pts.begin(), pts.end());
    sort(px.begin(), px.end(), compare_x);
    sort(py.begin(), py.end(), compare_y);
    return rcp(px, py);
}


int main(){
    cin >> N;
    vector<pdd>pts;
    for(int i = 0;i < N;i++){
        double x,y;
        cin >> x >> y;
        pts.push_back(make_pair(x,y)); 
    }
    return 0;
}
