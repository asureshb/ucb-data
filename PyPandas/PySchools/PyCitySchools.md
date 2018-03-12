

```python
import pandas as pd
```


```python
schoolfile = "schools_complete.csv"
school_pd = pd.read_csv(schoolfile, encoding = 'utf-8')
school_pd.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_school = school_pd['name'].count()
total_school
```




    15




```python
total_budget = school_pd['budget'].sum()
total_budget
```




    24649428




```python
studentfile = "students_complete.csv"
student_pd = pd.read_csv(studentfile)
student_pd.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_student=student_pd['name'].count()
total_student
```




    39170




```python
average_math_score = student_pd['math_score'].mean()
average_math_score
```




    78.98537145774827




```python
average_reading_score = student_pd['reading_score'].mean()
average_reading_score
```




    81.87784018381414




```python
# Passing math score = 70
passing_math_df=student_pd.loc[(student_pd["math_score"] >=70)]
passing_math_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Sheena Carter</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>82</td>
      <td>80</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Michael Roth</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>95</td>
      <td>87</td>
    </tr>
  </tbody>
</table>
</div>




```python
#passing reading score = 70
passing_reading_df=student_pd.loc[(student_pd["reading_score"] >= 70)]
passing_reading_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Sheena Carter</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>82</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
passing_math_student=passing_math_df['name'].count()
passing_math_percent =passing_math_student/total_student
passing_math_percent
```




    0.74980852693387801




```python
passing_reading_student = passing_reading_df['name'].count()
passing_reading_percent = passing_reading_student/total_student
passing_reading_percent
```




    0.85805463364820012




```python
overall_passing_rate = (passing_math_student + passing_reading_student)/ total_student
overall_passing_rate
```




    1.6078631605820781




```python
district_summary_df = pd.DataFrame({"Total Schools":[total_school],
                            "Total Students":[total_student],
                            "Total School Budget":["${:.2f}".format(total_budget)],
                            "Average Math Score":["{0:.2f}".format(average_math_score)],
                            "Average Reading Score":["{0:.2f}".format(average_reading_score)],
                            "% Passing Math":["{0:.2%}".format(passing_math_percent)],
                            "% Passing Reading":["{0:.2%}".format(passing_reading_percent)]
                            
                     })
print("District Summary")
district_summary_df
```

    District Summary
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Total School Budget</th>
      <th>Total Schools</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>74.98%</td>
      <td>85.81%</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>$24649428.00</td>
      <td>15</td>
      <td>39170</td>
    </tr>
  </tbody>
</table>
</div>




```python
reading_average_byschool=student_pd.groupby(['school'],as_index=False)['reading_score'].mean()
reading_average_byschool
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>reading_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.033963</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.975780</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.158020</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.746258</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.816757</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.934412</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.814988</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.182722</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.966394</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.044699</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.744686</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.725724</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.848930</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.989488</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.955000</td>
    </tr>
  </tbody>
</table>
</div>




```python
math_average_byschool=student_pd.groupby(['school'],as_index=False)['math_score'].mean()
math_average_byschool
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>77.048432</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.061895</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>76.711767</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>77.102592</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.351499</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>77.289752</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.803279</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>76.629414</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>77.072464</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83.839917</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>76.842711</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.359455</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.418349</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.274201</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.682222</td>
    </tr>
  </tbody>
</table>
</div>




```python
group_by_school_df = student_pd.groupby(['school'])
group_by_school_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>2917</th>
      <td>2917</td>
      <td>Amy Jacobs</td>
      <td>F</td>
      <td>10th</td>
      <td>Figueroa High School</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>2918</th>
      <td>2918</td>
      <td>Nathan Campbell</td>
      <td>M</td>
      <td>12th</td>
      <td>Figueroa High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>2919</th>
      <td>2919</td>
      <td>Randall Stewart</td>
      <td>M</td>
      <td>12th</td>
      <td>Figueroa High School</td>
      <td>67</td>
      <td>77</td>
    </tr>
    <tr>
      <th>2920</th>
      <td>2920</td>
      <td>Jennifer Brown</td>
      <td>F</td>
      <td>9th</td>
      <td>Figueroa High School</td>
      <td>97</td>
      <td>64</td>
    </tr>
    <tr>
      <th>2921</th>
      <td>2921</td>
      <td>Denise Lopez</td>
      <td>F</td>
      <td>10th</td>
      <td>Figueroa High School</td>
      <td>79</td>
      <td>64</td>
    </tr>
    <tr>
      <th>5866</th>
      <td>5866</td>
      <td>Jamie Montgomery</td>
      <td>F</td>
      <td>12th</td>
      <td>Shelton High School</td>
      <td>70</td>
      <td>91</td>
    </tr>
    <tr>
      <th>5867</th>
      <td>5867</td>
      <td>Shannon Phillips</td>
      <td>F</td>
      <td>10th</td>
      <td>Shelton High School</td>
      <td>84</td>
      <td>71</td>
    </tr>
    <tr>
      <th>5868</th>
      <td>5868</td>
      <td>Todd Barber</td>
      <td>M</td>
      <td>11th</td>
      <td>Shelton High School</td>
      <td>95</td>
      <td>99</td>
    </tr>
    <tr>
      <th>5869</th>
      <td>5869</td>
      <td>Desiree King</td>
      <td>F</td>
      <td>12th</td>
      <td>Shelton High School</td>
      <td>76</td>
      <td>95</td>
    </tr>
    <tr>
      <th>5870</th>
      <td>5870</td>
      <td>Melissa Roberts</td>
      <td>F</td>
      <td>10th</td>
      <td>Shelton High School</td>
      <td>71</td>
      <td>82</td>
    </tr>
    <tr>
      <th>7627</th>
      <td>7627</td>
      <td>Russell Davis</td>
      <td>M</td>
      <td>10th</td>
      <td>Hernandez High School</td>
      <td>70</td>
      <td>88</td>
    </tr>
    <tr>
      <th>7628</th>
      <td>7628</td>
      <td>Timothy Walker</td>
      <td>M</td>
      <td>12th</td>
      <td>Hernandez High School</td>
      <td>97</td>
      <td>93</td>
    </tr>
    <tr>
      <th>7629</th>
      <td>7629</td>
      <td>Katie Johnston</td>
      <td>F</td>
      <td>12th</td>
      <td>Hernandez High School</td>
      <td>83</td>
      <td>81</td>
    </tr>
    <tr>
      <th>7630</th>
      <td>7630</td>
      <td>Joann Oconnell</td>
      <td>F</td>
      <td>12th</td>
      <td>Hernandez High School</td>
      <td>77</td>
      <td>91</td>
    </tr>
    <tr>
      <th>7631</th>
      <td>7631</td>
      <td>Sarah Alexander</td>
      <td>F</td>
      <td>10th</td>
      <td>Hernandez High School</td>
      <td>84</td>
      <td>93</td>
    </tr>
    <tr>
      <th>12262</th>
      <td>12262</td>
      <td>Heather Wright</td>
      <td>F</td>
      <td>11th</td>
      <td>Griffin High School</td>
      <td>79</td>
      <td>68</td>
    </tr>
    <tr>
      <th>12263</th>
      <td>12263</td>
      <td>Elizabeth Goodwin</td>
      <td>F</td>
      <td>10th</td>
      <td>Griffin High School</td>
      <td>91</td>
      <td>81</td>
    </tr>
    <tr>
      <th>12264</th>
      <td>12264</td>
      <td>Michelle Wong</td>
      <td>F</td>
      <td>9th</td>
      <td>Griffin High School</td>
      <td>78</td>
      <td>89</td>
    </tr>
    <tr>
      <th>12265</th>
      <td>12265</td>
      <td>Scott Roth MD</td>
      <td>M</td>
      <td>11th</td>
      <td>Griffin High School</td>
      <td>91</td>
      <td>85</td>
    </tr>
    <tr>
      <th>12266</th>
      <td>12266</td>
      <td>Billy Wilson</td>
      <td>M</td>
      <td>12th</td>
      <td>Griffin High School</td>
      <td>76</td>
      <td>83</td>
    </tr>
    <tr>
      <th>13730</th>
      <td>13730</td>
      <td>Kelli Anderson</td>
      <td>F</td>
      <td>10th</td>
      <td>Wilson High School</td>
      <td>84</td>
      <td>71</td>
    </tr>
    <tr>
      <th>13731</th>
      <td>13731</td>
      <td>Russell Ramirez</td>
      <td>M</td>
      <td>10th</td>
      <td>Wilson High School</td>
      <td>72</td>
      <td>87</td>
    </tr>
    <tr>
      <th>13732</th>
      <td>13732</td>
      <td>Eric Butler</td>
      <td>M</td>
      <td>10th</td>
      <td>Wilson High School</td>
      <td>97</td>
      <td>82</td>
    </tr>
    <tr>
      <th>13733</th>
      <td>13733</td>
      <td>Warren Kerr</td>
      <td>M</td>
      <td>11th</td>
      <td>Wilson High School</td>
      <td>93</td>
      <td>68</td>
    </tr>
    <tr>
      <th>13734</th>
      <td>13734</td>
      <td>Gail Hall</td>
      <td>F</td>
      <td>9th</td>
      <td>Wilson High School</td>
      <td>79</td>
      <td>72</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>23274</th>
      <td>23274</td>
      <td>Alec Davis</td>
      <td>M</td>
      <td>9th</td>
      <td>Pena High School</td>
      <td>91</td>
      <td>75</td>
    </tr>
    <tr>
      <th>23275</th>
      <td>23275</td>
      <td>Michael Meyer</td>
      <td>M</td>
      <td>10th</td>
      <td>Pena High School</td>
      <td>94</td>
      <td>76</td>
    </tr>
    <tr>
      <th>23276</th>
      <td>23276</td>
      <td>Donald Gutierrez</td>
      <td>M</td>
      <td>11th</td>
      <td>Pena High School</td>
      <td>98</td>
      <td>91</td>
    </tr>
    <tr>
      <th>23277</th>
      <td>23277</td>
      <td>Travis Chavez</td>
      <td>M</td>
      <td>11th</td>
      <td>Pena High School</td>
      <td>78</td>
      <td>71</td>
    </tr>
    <tr>
      <th>23278</th>
      <td>23278</td>
      <td>Sheena Ball</td>
      <td>F</td>
      <td>12th</td>
      <td>Pena High School</td>
      <td>87</td>
      <td>92</td>
    </tr>
    <tr>
      <th>24236</th>
      <td>24236</td>
      <td>Aaron Johnson</td>
      <td>M</td>
      <td>10th</td>
      <td>Wright High School</td>
      <td>89</td>
      <td>72</td>
    </tr>
    <tr>
      <th>24237</th>
      <td>24237</td>
      <td>Kimberly Hamilton</td>
      <td>F</td>
      <td>10th</td>
      <td>Wright High School</td>
      <td>84</td>
      <td>93</td>
    </tr>
    <tr>
      <th>24238</th>
      <td>24238</td>
      <td>Ashley Johns</td>
      <td>F</td>
      <td>10th</td>
      <td>Wright High School</td>
      <td>88</td>
      <td>88</td>
    </tr>
    <tr>
      <th>24239</th>
      <td>24239</td>
      <td>Stephanie Donovan</td>
      <td>F</td>
      <td>10th</td>
      <td>Wright High School</td>
      <td>75</td>
      <td>84</td>
    </tr>
    <tr>
      <th>24240</th>
      <td>24240</td>
      <td>Cynthia Guzman</td>
      <td>F</td>
      <td>11th</td>
      <td>Wright High School</td>
      <td>93</td>
      <td>82</td>
    </tr>
    <tr>
      <th>26036</th>
      <td>26036</td>
      <td>Sherry Jenkins</td>
      <td>F</td>
      <td>11th</td>
      <td>Rodriguez High School</td>
      <td>74</td>
      <td>81</td>
    </tr>
    <tr>
      <th>26037</th>
      <td>26037</td>
      <td>Kimberly Calderon</td>
      <td>F</td>
      <td>10th</td>
      <td>Rodriguez High School</td>
      <td>80</td>
      <td>86</td>
    </tr>
    <tr>
      <th>26038</th>
      <td>26038</td>
      <td>William Brady</td>
      <td>M</td>
      <td>11th</td>
      <td>Rodriguez High School</td>
      <td>97</td>
      <td>62</td>
    </tr>
    <tr>
      <th>26039</th>
      <td>26039</td>
      <td>Jacob Padilla</td>
      <td>M</td>
      <td>11th</td>
      <td>Rodriguez High School</td>
      <td>79</td>
      <td>73</td>
    </tr>
    <tr>
      <th>26040</th>
      <td>26040</td>
      <td>Paula Maldonado</td>
      <td>F</td>
      <td>10th</td>
      <td>Rodriguez High School</td>
      <td>96</td>
      <td>92</td>
    </tr>
    <tr>
      <th>30035</th>
      <td>30035</td>
      <td>Lisa Casey</td>
      <td>F</td>
      <td>12th</td>
      <td>Johnson High School</td>
      <td>87</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30036</th>
      <td>30036</td>
      <td>Jessica Lopez</td>
      <td>F</td>
      <td>9th</td>
      <td>Johnson High School</td>
      <td>98</td>
      <td>62</td>
    </tr>
    <tr>
      <th>30037</th>
      <td>30037</td>
      <td>Anna Wilkins</td>
      <td>F</td>
      <td>11th</td>
      <td>Johnson High School</td>
      <td>89</td>
      <td>77</td>
    </tr>
    <tr>
      <th>30038</th>
      <td>30038</td>
      <td>Andrew Smith</td>
      <td>M</td>
      <td>9th</td>
      <td>Johnson High School</td>
      <td>66</td>
      <td>85</td>
    </tr>
    <tr>
      <th>30039</th>
      <td>30039</td>
      <td>Robert Allison</td>
      <td>M</td>
      <td>11th</td>
      <td>Johnson High School</td>
      <td>63</td>
      <td>85</td>
    </tr>
    <tr>
      <th>34796</th>
      <td>34796</td>
      <td>Michael Mercado</td>
      <td>M</td>
      <td>9th</td>
      <td>Ford High School</td>
      <td>66</td>
      <td>94</td>
    </tr>
    <tr>
      <th>34797</th>
      <td>34797</td>
      <td>Stephen Wolf</td>
      <td>M</td>
      <td>11th</td>
      <td>Ford High School</td>
      <td>68</td>
      <td>63</td>
    </tr>
    <tr>
      <th>34798</th>
      <td>34798</td>
      <td>Bonnie Hughes</td>
      <td>F</td>
      <td>12th</td>
      <td>Ford High School</td>
      <td>73</td>
      <td>59</td>
    </tr>
    <tr>
      <th>34799</th>
      <td>34799</td>
      <td>Melissa Smith</td>
      <td>F</td>
      <td>11th</td>
      <td>Ford High School</td>
      <td>88</td>
      <td>58</td>
    </tr>
    <tr>
      <th>34800</th>
      <td>34800</td>
      <td>Brian Mitchell</td>
      <td>M</td>
      <td>10th</td>
      <td>Ford High School</td>
      <td>96</td>
      <td>55</td>
    </tr>
    <tr>
      <th>37535</th>
      <td>37535</td>
      <td>Norma Mata</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>76</td>
      <td>76</td>
    </tr>
    <tr>
      <th>37536</th>
      <td>37536</td>
      <td>Cody Miller</td>
      <td>M</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>84</td>
      <td>82</td>
    </tr>
    <tr>
      <th>37537</th>
      <td>37537</td>
      <td>Erik Snyder</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>80</td>
      <td>90</td>
    </tr>
    <tr>
      <th>37538</th>
      <td>37538</td>
      <td>Tanya Martinez</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>71</td>
      <td>69</td>
    </tr>
    <tr>
      <th>37539</th>
      <td>37539</td>
      <td>Noah Erickson</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>86</td>
      <td>76</td>
    </tr>
  </tbody>
</table>
<p>75 rows × 7 columns</p>
</div>




```python
school_describe_df = group_by_school_df.describe()
school_describe_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">Student ID</th>
      <th colspan="5" halign="left">math_score</th>
      <th colspan="8" halign="left">reading_score</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>...</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>4976.0</td>
      <td>20358.5</td>
      <td>1436.591800</td>
      <td>17871.0</td>
      <td>19114.75</td>
      <td>20358.5</td>
      <td>21602.25</td>
      <td>22846.0</td>
      <td>4976.0</td>
      <td>77.048432</td>
      <td>...</td>
      <td>88.0</td>
      <td>99.0</td>
      <td>4976.0</td>
      <td>81.033963</td>
      <td>10.534034</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>1858.0</td>
      <td>16941.5</td>
      <td>536.502718</td>
      <td>16013.0</td>
      <td>16477.25</td>
      <td>16941.5</td>
      <td>17405.75</td>
      <td>17870.0</td>
      <td>1858.0</td>
      <td>83.061895</td>
      <td>...</td>
      <td>91.0</td>
      <td>99.0</td>
      <td>1858.0</td>
      <td>83.975780</td>
      <td>8.914236</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>2949.0</td>
      <td>4391.0</td>
      <td>851.447297</td>
      <td>2917.0</td>
      <td>3654.00</td>
      <td>4391.0</td>
      <td>5128.00</td>
      <td>5865.0</td>
      <td>2949.0</td>
      <td>76.711767</td>
      <td>...</td>
      <td>88.0</td>
      <td>99.0</td>
      <td>2949.0</td>
      <td>81.158020</td>
      <td>10.695019</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>2739.0</td>
      <td>36165.0</td>
      <td>790.825518</td>
      <td>34796.0</td>
      <td>35480.50</td>
      <td>36165.0</td>
      <td>36849.50</td>
      <td>37534.0</td>
      <td>2739.0</td>
      <td>77.102592</td>
      <td>...</td>
      <td>88.0</td>
      <td>99.0</td>
      <td>2739.0</td>
      <td>80.746258</td>
      <td>10.695989</td>
      <td>63.0</td>
      <td>71.5</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>1468.0</td>
      <td>12995.5</td>
      <td>423.919411</td>
      <td>12262.0</td>
      <td>12628.75</td>
      <td>12995.5</td>
      <td>13362.25</td>
      <td>13729.0</td>
      <td>1468.0</td>
      <td>83.351499</td>
      <td>...</td>
      <td>91.0</td>
      <td>99.0</td>
      <td>1468.0</td>
      <td>83.816757</td>
      <td>8.980237</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>




```python
math_group_by_school_df = school_describe_df['math_score']
#math_group_by_school_df.rename(columns={'mean':'Average Math Score'})
math_group_by_school_df.reset_index(level=0, inplace=True)
math_group_by_school_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>4976.0</td>
      <td>77.048432</td>
      <td>12.908393</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>77.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1858.0</td>
      <td>83.061895</td>
      <td>9.245293</td>
      <td>68.0</td>
      <td>75.0</td>
      <td>83.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>2949.0</td>
      <td>76.711767</td>
      <td>12.986908</td>
      <td>55.0</td>
      <td>65.0</td>
      <td>76.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>2739.0</td>
      <td>77.102592</td>
      <td>12.789984</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>77.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1468.0</td>
      <td>83.351499</td>
      <td>9.236004</td>
      <td>68.0</td>
      <td>75.0</td>
      <td>83.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>4635.0</td>
      <td>77.289752</td>
      <td>13.178957</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>77.0</td>
      <td>89.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>427.0</td>
      <td>83.803279</td>
      <td>9.342150</td>
      <td>68.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>93.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>2917.0</td>
      <td>76.629414</td>
      <td>12.947801</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>76.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>4761.0</td>
      <td>77.072464</td>
      <td>13.101575</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>77.0</td>
      <td>89.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>962.0</td>
      <td>83.839917</td>
      <td>9.326506</td>
      <td>68.0</td>
      <td>75.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>3999.0</td>
      <td>76.842711</td>
      <td>12.912722</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>77.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>1761.0</td>
      <td>83.359455</td>
      <td>9.142479</td>
      <td>68.0</td>
      <td>76.0</td>
      <td>83.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>1635.0</td>
      <td>83.418349</td>
      <td>9.280474</td>
      <td>68.0</td>
      <td>75.0</td>
      <td>83.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>2283.0</td>
      <td>83.274201</td>
      <td>9.141318</td>
      <td>68.0</td>
      <td>75.0</td>
      <td>83.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>1800.0</td>
      <td>83.682222</td>
      <td>9.221089</td>
      <td>68.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
reading_group_by_school_df = school_describe_df['reading_score']
reading_group_by_school_df.reset_index(level=0, inplace=True)
#reading_group_by_school_df.rename(columns={'mean':'Average Reading Score'})
reading_group_by_school_df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>4976.0</td>
      <td>81.033963</td>
      <td>10.534034</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1858.0</td>
      <td>83.975780</td>
      <td>8.914236</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>2949.0</td>
      <td>81.158020</td>
      <td>10.695019</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>2739.0</td>
      <td>80.746258</td>
      <td>10.695989</td>
      <td>63.0</td>
      <td>71.5</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1468.0</td>
      <td>83.816757</td>
      <td>8.980237</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>4635.0</td>
      <td>80.934412</td>
      <td>10.720988</td>
      <td>63.0</td>
      <td>71.5</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>427.0</td>
      <td>83.814988</td>
      <td>9.095010</td>
      <td>69.0</td>
      <td>75.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>2917.0</td>
      <td>81.182722</td>
      <td>10.655466</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>82.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>4761.0</td>
      <td>80.966394</td>
      <td>10.633946</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>962.0</td>
      <td>84.044699</td>
      <td>9.080349</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>3999.0</td>
      <td>80.744686</td>
      <td>10.656611</td>
      <td>63.0</td>
      <td>71.5</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>1761.0</td>
      <td>83.725724</td>
      <td>8.996038</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>83.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>1635.0</td>
      <td>83.848930</td>
      <td>8.974590</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>2283.0</td>
      <td>83.989488</td>
      <td>8.879753</td>
      <td>69.0</td>
      <td>77.0</td>
      <td>84.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>1800.0</td>
      <td>83.955000</td>
      <td>8.843000</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
math_percent_group_by_school= pd.DataFrame(group_by_school_df.apply(lambda x:(x.math_score>=70).sum()/x.math_score.count()))
math_percent_group_by_school.reset_index(inplace=True)
math_percent_group_by_school
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>0.666801</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>0.941335</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>0.659885</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>0.683096</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>0.933924</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>0.667530</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>0.925059</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>0.656839</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>0.660576</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>0.945946</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>0.663666</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>0.938671</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>0.932722</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>0.938677</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>0.933333</td>
    </tr>
  </tbody>
</table>
</div>




```python
reading_passing_rate_df = pd.DataFrame(group_by_school_df.apply(lambda x:(x.reading_score>=70).sum()/x.reading_score.count()))
reading_passing_rate_df.reset_index(inplace=True)
reading_passing_rate_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>0.819333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>0.970398</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>0.807392</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>0.792990</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>0.971390</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>0.808630</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>0.962529</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>0.813164</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>0.812224</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>0.959459</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>0.802201</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>0.958546</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>0.973089</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>0.965396</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>0.966111</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_summary_1_df = pd.merge(reading_group_by_school_df,math_group_by_school_df,on='school')
school_summary_1_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>count_x</th>
      <th>mean_x</th>
      <th>std_x</th>
      <th>min_x</th>
      <th>25%_x</th>
      <th>50%_x</th>
      <th>75%_x</th>
      <th>max_x</th>
      <th>count_y</th>
      <th>mean_y</th>
      <th>std_y</th>
      <th>min_y</th>
      <th>25%_y</th>
      <th>50%_y</th>
      <th>75%_y</th>
      <th>max_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>4976.0</td>
      <td>81.033963</td>
      <td>10.534034</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
      <td>4976.0</td>
      <td>77.048432</td>
      <td>12.908393</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>77.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1858.0</td>
      <td>83.975780</td>
      <td>8.914236</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>92.0</td>
      <td>99.0</td>
      <td>1858.0</td>
      <td>83.061895</td>
      <td>9.245293</td>
      <td>68.0</td>
      <td>75.0</td>
      <td>83.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>2949.0</td>
      <td>81.158020</td>
      <td>10.695019</td>
      <td>63.0</td>
      <td>72.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
      <td>2949.0</td>
      <td>76.711767</td>
      <td>12.986908</td>
      <td>55.0</td>
      <td>65.0</td>
      <td>76.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>2739.0</td>
      <td>80.746258</td>
      <td>10.695989</td>
      <td>63.0</td>
      <td>71.5</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>99.0</td>
      <td>2739.0</td>
      <td>77.102592</td>
      <td>12.789984</td>
      <td>55.0</td>
      <td>66.0</td>
      <td>77.0</td>
      <td>88.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1468.0</td>
      <td>83.816757</td>
      <td>8.980237</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>84.0</td>
      <td>91.0</td>
      <td>99.0</td>
      <td>1468.0</td>
      <td>83.351499</td>
      <td>9.236004</td>
      <td>68.0</td>
      <td>75.0</td>
      <td>83.0</td>
      <td>91.0</td>
      <td>99.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_summary_2_df=school_summary_1_df[['school','mean_x','mean_y']]
```


```python
school_pd_rename = school_pd.rename(columns={'name':'school'})
school_summary_3_df = pd.merge(school_summary_2_df,school_pd_rename,on='school')
school_summary_3_df['perstudentbudget']=school_summary_3_df['budget']/school_summary_3_df['size']
school_summary_3_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>mean_x</th>
      <th>mean_y</th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>perstudentbudget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>7</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>6</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>1</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>13</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>4</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>3</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>8</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>12</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>9</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>11</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>5</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>10</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
percent_passing_summary= pd.merge(reading_passing_rate_df,math_percent_group_by_school,on='school')
percent_passing_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>0_x</th>
      <th>0_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>0.819333</td>
      <td>0.666801</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>0.970398</td>
      <td>0.941335</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>0.807392</td>
      <td>0.659885</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>0.792990</td>
      <td>0.683096</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>0.971390</td>
      <td>0.933924</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>0.808630</td>
      <td>0.667530</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>0.962529</td>
      <td>0.925059</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>0.813164</td>
      <td>0.656839</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>0.812224</td>
      <td>0.660576</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>0.959459</td>
      <td>0.945946</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>0.802201</td>
      <td>0.663666</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>0.958546</td>
      <td>0.938671</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>0.973089</td>
      <td>0.932722</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>0.965396</td>
      <td>0.938677</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>0.966111</td>
      <td>0.933333</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_summary = pd.merge(school_summary_3_df,percent_passing_summary,on='school')
school_summary['mean_x']=school_summary['mean_x'].map("{:.2f}".format)
school_summary['mean_y']=school_summary['mean_y'].map("{:.2f}".format)
school_summary['Overall Passing Rate']=(school_summary['0_x']+school_summary['0_y'])/2
school_summary['0_x']=school_summary['0_x'].map("{:,.2%}".format)
school_summary['0_y']=school_summary['0_y'].map("{:,.2%}".format)
school_summary['Overall Passing Rate']=school_summary['Overall Passing Rate'].map("{:,.2%}".format)
school_summary_final = school_summary.rename(columns={'mean_x':'Average Reading Score','mean_y':'Average Math Score','0_x':'% Passing Reading','0_y':'% Passing Math','perstudentbudget':'Per Student Budget'})
school_summary_final = school_summary_final.iloc[:,[0,1,2,4,5,6,7,8,9,10]]
print("School Summary")
school_summary_final
```

    School Summary
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.03</td>
      <td>77.05</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>81.93%</td>
      <td>66.68%</td>
      <td>74.31%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.98</td>
      <td>83.06</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>97.04%</td>
      <td>94.13%</td>
      <td>95.59%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.16</td>
      <td>76.71</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>80.74%</td>
      <td>65.99%</td>
      <td>73.36%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.75</td>
      <td>77.10</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>79.30%</td>
      <td>68.31%</td>
      <td>73.80%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.82</td>
      <td>83.35</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>97.14%</td>
      <td>93.39%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.93</td>
      <td>77.29</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>80.86%</td>
      <td>66.75%</td>
      <td>73.81%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.81</td>
      <td>83.80</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>96.25%</td>
      <td>92.51%</td>
      <td>94.38%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.18</td>
      <td>76.63</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.32%</td>
      <td>65.68%</td>
      <td>73.50%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.97</td>
      <td>77.07</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>81.22%</td>
      <td>66.06%</td>
      <td>73.64%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.04</td>
      <td>83.84</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>95.95%</td>
      <td>94.59%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.74</td>
      <td>76.84</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.22%</td>
      <td>66.37%</td>
      <td>73.29%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.73</td>
      <td>83.36</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>95.85%</td>
      <td>93.87%</td>
      <td>94.86%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.85</td>
      <td>83.42</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>97.31%</td>
      <td>93.27%</td>
      <td>95.29%</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.99</td>
      <td>83.27</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>96.54%</td>
      <td>93.87%</td>
      <td>95.20%</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.95</td>
      <td>83.68</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>96.61%</td>
      <td>93.33%</td>
      <td>94.97%</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_5_school = school_summary_final.sort_values(['Overall Passing Rate'], ascending=False)
print("Top Performing Schools (By Passing Rate)")
top_5_school.head(5)
```

    Top Performing Schools (By Passing Rate)
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.98</td>
      <td>83.06</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>97.04%</td>
      <td>94.13%</td>
      <td>95.59%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.85</td>
      <td>83.42</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>97.31%</td>
      <td>93.27%</td>
      <td>95.29%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.82</td>
      <td>83.35</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>97.14%</td>
      <td>93.39%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.04</td>
      <td>83.84</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>95.95%</td>
      <td>94.59%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.99</td>
      <td>83.27</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>96.54%</td>
      <td>93.87%</td>
      <td>95.20%</td>
    </tr>
  </tbody>
</table>
</div>




```python
bottom_5_school = school_summary_final.sort_values(['Overall Passing Rate'])
print("Bottom 5 Performing Schools" )
bottom_5_school.head(5)
```

    Bottom 5 Performing Schools
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.74</td>
      <td>76.84</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.22%</td>
      <td>66.37%</td>
      <td>73.29%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.16</td>
      <td>76.71</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>80.74%</td>
      <td>65.99%</td>
      <td>73.36%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.18</td>
      <td>76.63</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.32%</td>
      <td>65.68%</td>
      <td>73.50%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.97</td>
      <td>77.07</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>81.22%</td>
      <td>66.06%</td>
      <td>73.64%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.75</td>
      <td>77.10</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>79.30%</td>
      <td>68.31%</td>
      <td>73.80%</td>
    </tr>
  </tbody>
</table>
</div>




```python
math_average_group_by_grade_1_df = student_pd.groupby(['school','grade'])['math_score'].mean()
math_average_group_by_grade_df= pd.DataFrame(math_average_group_by_grade_1_df)
print("Math Scores by Grade")
math_average_group_by_grade_df
```

    Math Scores by Grade
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>math_score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>76.996772</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.515588</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.083676</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Cabrera High School</th>
      <th>10th</th>
      <td>83.154506</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>82.765560</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.094697</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Figueroa High School</th>
      <th>10th</th>
      <td>76.539974</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.884344</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.403037</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Ford High School</th>
      <th>10th</th>
      <td>77.672316</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.918058</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.361345</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Griffin High School</th>
      <th>10th</th>
      <td>84.229064</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.842105</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>82.044010</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hernandez High School</th>
      <th>10th</th>
      <td>77.337408</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.136029</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.438495</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Holden High School</th>
      <th>10th</th>
      <td>83.429825</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>85.000000</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.787402</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Huang High School</th>
      <th>10th</th>
      <td>75.908735</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.446602</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.027251</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Johnson High School</th>
      <th>10th</th>
      <td>76.691117</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.491653</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.187857</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Pena High School</th>
      <th>10th</th>
      <td>83.372000</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.328125</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.625455</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Rodriguez High School</th>
      <th>10th</th>
      <td>76.612500</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.395626</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.859966</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Shelton High School</th>
      <th>10th</th>
      <td>82.917411</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.383495</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.420755</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Thomas High School</th>
      <th>10th</th>
      <td>83.087886</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.498795</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.590022</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wilson High School</th>
      <th>10th</th>
      <td>83.724422</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.195326</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.085578</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wright High School</th>
      <th>10th</th>
      <td>84.010288</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.836782</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.644986</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
reading_average_group_by_grade_1_df = student_pd.groupby(['school','grade'])['reading_score'].mean()
reading_average_group_by_grade_df= pd.DataFrame(reading_average_group_by_grade_1_df)
print("Math Scores by Grade")
reading_average_group_by_grade_df
```

    Math Scores by Grade
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>reading_score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>80.907183</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.945643</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.303155</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Cabrera High School</th>
      <th>10th</th>
      <td>84.253219</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.788382</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.676136</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Figueroa High School</th>
      <th>10th</th>
      <td>81.408912</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.640339</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.198598</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Ford High School</th>
      <th>10th</th>
      <td>81.262712</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.403642</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.632653</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Griffin High School</th>
      <th>10th</th>
      <td>83.706897</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.288089</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.369193</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hernandez High School</th>
      <th>10th</th>
      <td>80.660147</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.396140</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.866860</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Holden High School</th>
      <th>10th</th>
      <td>83.324561</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.815534</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.677165</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Huang High School</th>
      <th>10th</th>
      <td>81.512386</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.417476</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.290284</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Johnson High School</th>
      <th>10th</th>
      <td>80.773431</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.616027</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.260714</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Pena High School</th>
      <th>10th</th>
      <td>83.612000</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.335938</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.807273</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Rodriguez High School</th>
      <th>10th</th>
      <td>80.629808</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.864811</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.993127</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Shelton High School</th>
      <th>10th</th>
      <td>83.441964</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.373786</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>84.122642</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Thomas High School</th>
      <th>10th</th>
      <td>84.254157</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.585542</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.728850</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wilson High School</th>
      <th>10th</th>
      <td>84.021452</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.764608</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.939778</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wright High School</th>
      <th>10th</th>
      <td>83.812757</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.156322</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.073171</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.833333</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(school_summary_final['Per Student Budget'].max())
print(school_summary_final['Per Student Budget'].min())
```

    655.0
    578.0
    


```python
bins = [575,595,615,635,655] # based on school budget per student

# Create labels for these bins
group_labels = ["575-595","595-615","615-635","635-655"]
```


```python
school_summary_final["Average Spending Range"] = pd.cut(school_summary_final['Per Student Budget'],bins,labels=group_labels)
score_by_school_spending_df = school_summary_final.iloc[:,[0,1,2,6,7,8,9,10]]
print("Scores by School Spending")
score_by_school_spending_df
```

    Scores by School Spending
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>Per Student Budget</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
      <th>Average Spending Range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.03</td>
      <td>77.05</td>
      <td>628.0</td>
      <td>81.93%</td>
      <td>66.68%</td>
      <td>74.31%</td>
      <td>615-635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.98</td>
      <td>83.06</td>
      <td>582.0</td>
      <td>97.04%</td>
      <td>94.13%</td>
      <td>95.59%</td>
      <td>575-595</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.16</td>
      <td>76.71</td>
      <td>639.0</td>
      <td>80.74%</td>
      <td>65.99%</td>
      <td>73.36%</td>
      <td>635-655</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.75</td>
      <td>77.10</td>
      <td>644.0</td>
      <td>79.30%</td>
      <td>68.31%</td>
      <td>73.80%</td>
      <td>635-655</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.82</td>
      <td>83.35</td>
      <td>625.0</td>
      <td>97.14%</td>
      <td>93.39%</td>
      <td>95.27%</td>
      <td>615-635</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.93</td>
      <td>77.29</td>
      <td>652.0</td>
      <td>80.86%</td>
      <td>66.75%</td>
      <td>73.81%</td>
      <td>635-655</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.81</td>
      <td>83.80</td>
      <td>581.0</td>
      <td>96.25%</td>
      <td>92.51%</td>
      <td>94.38%</td>
      <td>575-595</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.18</td>
      <td>76.63</td>
      <td>655.0</td>
      <td>81.32%</td>
      <td>65.68%</td>
      <td>73.50%</td>
      <td>635-655</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.97</td>
      <td>77.07</td>
      <td>650.0</td>
      <td>81.22%</td>
      <td>66.06%</td>
      <td>73.64%</td>
      <td>635-655</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.04</td>
      <td>83.84</td>
      <td>609.0</td>
      <td>95.95%</td>
      <td>94.59%</td>
      <td>95.27%</td>
      <td>595-615</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.74</td>
      <td>76.84</td>
      <td>637.0</td>
      <td>80.22%</td>
      <td>66.37%</td>
      <td>73.29%</td>
      <td>635-655</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.73</td>
      <td>83.36</td>
      <td>600.0</td>
      <td>95.85%</td>
      <td>93.87%</td>
      <td>94.86%</td>
      <td>595-615</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.85</td>
      <td>83.42</td>
      <td>638.0</td>
      <td>97.31%</td>
      <td>93.27%</td>
      <td>95.29%</td>
      <td>635-655</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.99</td>
      <td>83.27</td>
      <td>578.0</td>
      <td>96.54%</td>
      <td>93.87%</td>
      <td>95.20%</td>
      <td>575-595</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.95</td>
      <td>83.68</td>
      <td>583.0</td>
      <td>96.61%</td>
      <td>93.33%</td>
      <td>94.97%</td>
      <td>575-595</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(school_pd['size'].max())
print(school_pd['size'].min())
```

    4976
    427
    


```python
bins = [400,2000,3500,5000] # based on school size

# Create labels for these bins
group_labels = ["Small: 400 to 2000","Medium: 2000 to 3500","Large: 3500 to 5000"]
```


```python
score_by_school_size_df = school_summary_final.iloc[:,[0,1,2,4,7,8,9]]
score_by_school_size_df["school size"] = pd.cut(score_by_school_size_df['size'],bins,labels=group_labels)
print("Scores by School Size")
score_by_school_size_df.sort_values(["school size"])
```

    Scores by School Size
    

    C:\ProgramData\Anaconda3\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>size</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
      <th>school size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.98</td>
      <td>83.06</td>
      <td>1858</td>
      <td>97.04%</td>
      <td>94.13%</td>
      <td>95.59%</td>
      <td>Small: 400 to 2000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.82</td>
      <td>83.35</td>
      <td>1468</td>
      <td>97.14%</td>
      <td>93.39%</td>
      <td>95.27%</td>
      <td>Small: 400 to 2000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.81</td>
      <td>83.80</td>
      <td>427</td>
      <td>96.25%</td>
      <td>92.51%</td>
      <td>94.38%</td>
      <td>Small: 400 to 2000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.04</td>
      <td>83.84</td>
      <td>962</td>
      <td>95.95%</td>
      <td>94.59%</td>
      <td>95.27%</td>
      <td>Small: 400 to 2000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.73</td>
      <td>83.36</td>
      <td>1761</td>
      <td>95.85%</td>
      <td>93.87%</td>
      <td>94.86%</td>
      <td>Small: 400 to 2000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.85</td>
      <td>83.42</td>
      <td>1635</td>
      <td>97.31%</td>
      <td>93.27%</td>
      <td>95.29%</td>
      <td>Small: 400 to 2000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.95</td>
      <td>83.68</td>
      <td>1800</td>
      <td>96.61%</td>
      <td>93.33%</td>
      <td>94.97%</td>
      <td>Small: 400 to 2000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.16</td>
      <td>76.71</td>
      <td>2949</td>
      <td>80.74%</td>
      <td>65.99%</td>
      <td>73.36%</td>
      <td>Medium: 2000 to 3500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.75</td>
      <td>77.10</td>
      <td>2739</td>
      <td>79.30%</td>
      <td>68.31%</td>
      <td>73.80%</td>
      <td>Medium: 2000 to 3500</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.18</td>
      <td>76.63</td>
      <td>2917</td>
      <td>81.32%</td>
      <td>65.68%</td>
      <td>73.50%</td>
      <td>Medium: 2000 to 3500</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.99</td>
      <td>83.27</td>
      <td>2283</td>
      <td>96.54%</td>
      <td>93.87%</td>
      <td>95.20%</td>
      <td>Medium: 2000 to 3500</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.03</td>
      <td>77.05</td>
      <td>4976</td>
      <td>81.93%</td>
      <td>66.68%</td>
      <td>74.31%</td>
      <td>Large: 3500 to 5000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.93</td>
      <td>77.29</td>
      <td>4635</td>
      <td>80.86%</td>
      <td>66.75%</td>
      <td>73.81%</td>
      <td>Large: 3500 to 5000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.97</td>
      <td>77.07</td>
      <td>4761</td>
      <td>81.22%</td>
      <td>66.06%</td>
      <td>73.64%</td>
      <td>Large: 3500 to 5000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.74</td>
      <td>76.84</td>
      <td>3999</td>
      <td>80.22%</td>
      <td>66.37%</td>
      <td>73.29%</td>
      <td>Large: 3500 to 5000</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_group_by_type_df = school_summary_final.iloc[:,[0,1,2,3,7,8,9]]
school_group_by_type_df = school_group_by_type_df.sort_values(['type'])
print("Scores by School Type")
school_group_by_type_df

```

    Scores by School Type
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>type</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.98</td>
      <td>83.06</td>
      <td>Charter</td>
      <td>97.04%</td>
      <td>94.13%</td>
      <td>95.59%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.82</td>
      <td>83.35</td>
      <td>Charter</td>
      <td>97.14%</td>
      <td>93.39%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.81</td>
      <td>83.80</td>
      <td>Charter</td>
      <td>96.25%</td>
      <td>92.51%</td>
      <td>94.38%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.04</td>
      <td>83.84</td>
      <td>Charter</td>
      <td>95.95%</td>
      <td>94.59%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.73</td>
      <td>83.36</td>
      <td>Charter</td>
      <td>95.85%</td>
      <td>93.87%</td>
      <td>94.86%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.85</td>
      <td>83.42</td>
      <td>Charter</td>
      <td>97.31%</td>
      <td>93.27%</td>
      <td>95.29%</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.99</td>
      <td>83.27</td>
      <td>Charter</td>
      <td>96.54%</td>
      <td>93.87%</td>
      <td>95.20%</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.95</td>
      <td>83.68</td>
      <td>Charter</td>
      <td>96.61%</td>
      <td>93.33%</td>
      <td>94.97%</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.03</td>
      <td>77.05</td>
      <td>District</td>
      <td>81.93%</td>
      <td>66.68%</td>
      <td>74.31%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.16</td>
      <td>76.71</td>
      <td>District</td>
      <td>80.74%</td>
      <td>65.99%</td>
      <td>73.36%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.75</td>
      <td>77.10</td>
      <td>District</td>
      <td>79.30%</td>
      <td>68.31%</td>
      <td>73.80%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.93</td>
      <td>77.29</td>
      <td>District</td>
      <td>80.86%</td>
      <td>66.75%</td>
      <td>73.81%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.18</td>
      <td>76.63</td>
      <td>District</td>
      <td>81.32%</td>
      <td>65.68%</td>
      <td>73.50%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.97</td>
      <td>77.07</td>
      <td>District</td>
      <td>81.22%</td>
      <td>66.06%</td>
      <td>73.64%</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.74</td>
      <td>76.84</td>
      <td>District</td>
      <td>80.22%</td>
      <td>66.37%</td>
      <td>73.29%</td>
    </tr>
  </tbody>
</table>
</div>


