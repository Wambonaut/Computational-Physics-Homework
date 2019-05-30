<pre><p>
#include &lt;math.h&gt;
#define NRANSI
#include &quot;nrutil.h&quot;

float pythag(float a, float b)
{
	float absa,absb;
	absa=fabs(a);
	absb=fabs(b);
	if (absa &gt; absb) return absa*sqrt(1.0+SQR(absb/absa));
	else return (absb == 0.0 ? 0.0 : absb*sqrt(1.0+SQR(absa/absb)));
}
#undef NRANSI
</p></pre>