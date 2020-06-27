#!/bin/sh

export AUTH0_DOMAIN='casting-agency-full-stack.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='casting-agency-full-stack'
export CLIENT_ID='05PDUxQbk8GV2eLEfOJlsC58sDxefb1D'

export producer_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM0Ym9OdGZaaEdZdTlHeThfWHBFRyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWZ1bGwtc3RhY2sudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjVhZGExN2NiYzg1MDAxOTJhMWU1ZSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWZ1bGwtc3RhY2siLCJpYXQiOjE1OTMzMTMyMzAsImV4cCI6MTU5MzMyMDQzMCwiYXpwIjoiMDVQRFV4UWJrOEdWMmVMRWZPSmxzQzU4c0R4ZWZiMUQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.FsT-ccql61Bns8SgCzs0aLYrievH_ZauTYgYx4Gku3bSJPW6srYYV0VmI7lqlRgw695h_-6lN0z0hTOJOzQVySjjtEW-3RxAxL01oOs4gis2vVmH3_QwvTK1beFruI5E3yd1A0NCDgmibUsU59V-V_kTMdhCT-rJpEQ61bVSB8jm4VmOtqMqt3AdRlY3cdoRs1roqp94-YAOCNnF9fLOijNtaKRgAhkML5KGXbaqudKHmK4bnWWF54iBPyq4iIOaStkYbbSXhDlAuZoXF1gTlC1WRq9Bwah4i7_y7a14uYxSUcRZ2Ivp96M-Kmqvt_NMkPiwZ314n9VwCgqvOQmgPA

export director_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM0Ym9OdGZaaEdZdTlHeThfWHBFRyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWZ1bGwtc3RhY2sudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjVhYzAyMjk5NTM2MDAxNDZhM2Q4MCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWZ1bGwtc3RhY2siLCJpYXQiOjE1OTMzMTI5MjgsImV4cCI6MTU5MzMyMDEyOCwiYXpwIjoiMDVQRFV4UWJrOEdWMmVMRWZPSmxzQzU4c0R4ZWZiMUQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.HjLuVzMeF_KnFPOf_NKHMSvo3_sh4TWpWKyiXcKLqXKOvXpJsImseKaX94jLMR3hg5QImfxQUHtM_8sE_v_qiUMZXCGaaeZ3Dar9bIggonkt2xbvlD1p4_VW1CHn7noZ_kZqUn5w4WViBXxNi2MSNla3MOGQDyHG7D5bX1ZzmZoD3tbMNgFGjpI1Yf6UVPgfnOs4MKMA_tvY-zT_o7n1se3SWcRnp6SkunQN_E5wWWWsKWuv4DkGeBW_MUizaQz7IwYdxkqZdWpyXsVsmr7HsX97T3XCm-982lu1FeVZVaMfW-hx-IZ4hubSRWNygLC0lae2Vo07I7Fk_wT1Lw_eYg

export assistant_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM0Ym9OdGZaaEdZdTlHeThfWHBFRyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWZ1bGwtc3RhY2sudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjVhYjllZjNjZTMyMDAxYTQwZWY5MCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWZ1bGwtc3RhY2siLCJpYXQiOjE1OTMzMTMxNzQsImV4cCI6MTU5MzMyMDM3NCwiYXpwIjoiMDVQRFV4UWJrOEdWMmVMRWZPSmxzQzU4c0R4ZWZiMUQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.vDFUObXualhKq4NxAhBh6mz4QH3gEEiYdZNz8HeiKondK49bTmtut5frP2uTEhwpr6bNbYxMZD-2U-L3A9ugSRcjmXjhbFjxCpM2wSblYIEl4cEG5jGurfE25Kck_bTh65JaeXGDhUG_M7JpKTdQtmFLDuziXE1nmGybOdDZKqsevwCX4SFBQ29WjIre3JfX91CGM5MumCVv52BfX4mdcoQmEj5TWQEPp74QBiMFzrpNutJv-z-gt8_L3-XiHH2Hbnb2qOb49-VuWrAxtTi1U5iR0Nt5mYm85KvAhpUmOf45MuWkNlntaLRgR-76Xi8-6jP6GDzdc2ex0jBy-CkncQ