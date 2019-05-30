#include <Python.h>
#include <math.h>
#define NRANSI
#include "nrutil.h"
// Householder reduction of a real, symmetric matrix a[1..n][1..n]. 
// On output, a is replaced by the orthogonal matrix Q effecting the
// transformation. d[1..n] returns the diagonal elements of the tridiagonal
// matrix, and e[1..e] the off-diagonal elements, with e[1]=0. Several
// statements, as noted in comments, can be omitted if only eigenvalues are to
// be found, in which case a contains no useful information on output. Otherwise
// they are included.
float pythag(float a, float b)
{
	float absa,absb;
	absa=fabs(a);
	absb=fabs(b);
	if (absa >= absb) return absa*sqrt(1.0+SQR(absb/absa));
	else return (absb == 0.0 ? 0.0 : absb*sqrt(1.0+SQR(absa/absb)));
}

void tred2_c(double **a, int n, double d[],double e[])
{
	int l,k,j,i;
        double scale,hh,h,g,f;
	for (i=n;i>=2;i--) {
		l=i-1;
		h=scale=0.0;
		if (l > 1) {
			for (k=1;k<=l;k++){
				printf("%i, %i\n", i,k);
				scale += fabs(a[i][k]);
			}
			if (scale == 0.0){
				e[i]=a[i][l]; 
			}
			else {
				for (k=1;k<=l;k++) {
					printf("%i,%i\n",i,k);
					a[i][k] /= scale;
					h += a[i][k]*a[i][k];
				}
				f=a[i][l];
				g=(f >= 0.0 ? -sqrt(h) : sqrt(h));
				e[i]=scale*g;
				h -= f*g;
				a[i][l]=f-g;
				f=0.0;
				for (j=1;j<=l;j++) {
					a[j][i]=a[i][j]/h;
					g=0.0;
					for (k=1;k<=j;k++)
						g += a[j][k]*a[i][k];
					for (k=j+1;k<=l;k++)
						g += a[k][j]*a[i][k];
					e[j]=g/h;
					f += e[j]*a[i][j];
				}
				hh=f/(h+h);
				for (j=1;j<=l;j++) {
					f=a[i][j];
					e[j]=g=e[j]-hh*f;
					for (k=1;k<=j;k++)
						a[j][k] -= (f*e[k]+g*a[i][k]);
				}
			}
		} else
			e[i]=a[i][l];
		d[i]=h;
	}
	d[1]=0.0;
	e[1]=0.0;
	/* Contents of this loop can be omitted if eigenvectors not
			wanted except for statement d[i]=a[i][i]; */
	for (i=1;i<=n;i++) {
		l=i-1;
		if (d[i]) {
			for (j=1;j<=l;j++) {
				g=0.0;
				for (k=1;k<=l;k++)
					g += a[i][k]*a[k][j];
				for (k=1;k<=l;k++)
					a[k][j] -= g*a[k][i];
			}
		}
		d[i]=a[i][i];
		a[i][i]=1.0;
		for (j=1;j<=l;j++) a[j][i]=a[i][j]=0.0;
	}

}

void tqli_c(float d[], float e[], int n, float **z)
{
	float pythag(float a, float b);
	int m,l,iter,i,k;
	float s,r,p,g,f,dd,c,b;

	for (i=2;i<=n;i++) e[i-1]=e[i];
	e[n]=0.0;
	for (l=1;l<=n;l++) {
		iter=0;
		do {
			for (m=l;m<=n-1;m++) {
				dd=fabs(d[m])+fabs(d[m+1]);
				if ((float)(fabs(e[m])+dd) == dd) break;
			}
			if (m != l) {
				g=(d[l+1]-d[l])/(2.0*e[l]);
				r=pythag(g,1.0);
				g=d[m]-d[l]+e[l]/(g+SIGN(r,g));
				s=c=1.0;
				p=0.0;
				for (i=m-1;i>=l;i--) {
					f=s*e[i];
					b=c*e[i];
					e[i+1]=(r=pythag(f,g));
					if (r == 0.0) {
						d[i+1] -= p;
						e[m]=0.0;
						break;
					}
					s=f/r;
					c=g/r;
					g=d[i+1]-p;
					r=(d[i]-g)*s+2.0*c*b;
					d[i+1]=g+(p=s*r);
					g=c*r-b;
					for (k=1;k<=n;k++) {
						f=z[k][i+1];
						z[k][i+1]=s*z[k][i]+c*f;
						z[k][i]=c*z[k][i]-s*f;
					}
				}
				if (r == 0.0 && i >= l) continue;
				d[l] -= p;
				e[l]=g;
				e[m]=0.0;
			}
		} while (m != l);
	}
}
static PyObject * tred2(PyObject *self, PyObject *args) {
	PyObject *pList;
	PyArg_ParseTuple(args, "O!", &PyList_Type, &pList);
	Py_ssize_t n=PyList_Size(pList)+1;
	double a[n][n];
	PyObject *pRow;
	PyObject *pElement;
	for(int j=1; j<n; j++){
		pRow=PyList_GetItem(pList,j-1);
		for(int i=1; i<n; i++){
			pElement = PyList_GetItem(pRow,i-1);
			a[j][i]=PyFloat_AsDouble(pElement);
		}
	}
	double *a_rows[n];
	for(int i=0; i<n; i++)
		a_rows[i]=a[i];
	double d[n];
	double e[n];
	double **aa=a_rows;
	tred2_c(aa, n-1, d, e);
	PyObject *a_py=PyList_New(n-1);
	PyObject *d_py=PyList_New(n-1);
	PyObject *e_py=PyList_New(n-1);
	PyObject *a_py_row;
	for(int j=1; j<n; j++){
		a_py_row=PyList_New(n-1);
		for(int i=1; i<n; i++){
			PyList_SetItem(a_py_row, i-1, PyFloat_FromDouble(aa[j][i]));
		}
		PyList_SetItem(a_py, j-1, a_py_row);
	}
	for(int i=1; i<n; i++){
		PyList_SetItem(e_py,i-1, PyFloat_FromDouble(e[i]));
		PyList_SetItem(d_py,i-1, PyFloat_FromDouble(d[i]));
	}
	PyObject *all=PyList_New(3);
	PyList_SetItem(all,0,a_py);
	PyList_SetItem(all,1,d_py);
	PyList_SetItem(all,2,e_py);
	return all;
}


static PyObject * tqli(PyObject *self, PyObject *args) {
	PyObject *pListD;
	PyObject *pListE;
	PyObject *pListZ;
	PyArg_ParseTuple(args, "O!O!O!", &PyList_Type, &pListD, &PyList_Type, &pListE, &PyList_Type,  &pListZ);
	Py_ssize_t n=PyList_Size(pListD)+1;
	
	float d[n];
	float e[n];
	for(int i=1; i<n; i++){
		d[i]=(float) PyFloat_AsDouble(PyList_GetItem(pListD,i-1));
		e[i]=(float) PyFloat_AsDouble(PyList_GetItem(pListE,i-1));
	}
	printf("1\n");	
	
	float a[n][n];
	PyObject *pRow;
	PyObject *pElement;
	for(int j=1; j<n; j++){
		pRow=PyList_GetItem(pListZ,j-1);
		for(int i=1; i<n; i++){
			pElement = PyList_GetItem(pRow,i-1);
			a[j][i]=(float) PyFloat_AsDouble(pElement);
			printf("Element %i, %i: %f\n", j, i,a[j][i]);
		}
	}
	float *a_rows[n];
	for(int i=0; i<n; i++)
		a_rows[i]=a[i];
	float **z=a_rows;
	

	tqli_c(d,e,n-1,z);
	PyObject *d_py=PyList_New(n-1);
	for(int i=1; i<n; i++){
		PyList_SetItem(d_py,i-1, PyFloat_FromDouble((double) d[i]));
	}
	
	PyObject *a_py=PyList_New(n-1);
	PyObject *a_py_row;
	for(int j=1; j<n; j++){
		a_py_row=PyList_New(n-1);
		for(int i=1; i<n; i++){
			PyList_SetItem(a_py_row, i-1, PyFloat_FromDouble((double) z[j][i]));
		}
		PyList_SetItem(a_py, j-1, a_py_row);
	}
	PyObject *all=PyList_New(2);
	PyList_SetItem(all, 0, d_py);
	PyList_SetItem(all, 1, a_py);
	return all;
}

static PyMethodDef numMethods[] = {
	{"tred2", tred2, METH_VARARGS,"Householder Reduction"},
	{"tqli", tqli, METH_VARARGS, "TQLI"},
	{NULL,NULL,0,NULL}
};
static struct PyModuleDef nummodule = {
	PyModuleDef_HEAD_INIT,
	"num",
	NULL,
	-1,
	numMethods
};
PyMODINIT_FUNC PyInit_num(void){
	return PyModule_Create(&nummodule);
}


/* (C) Copr. 1986-92 Numerical Recipes Software */

